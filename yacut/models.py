import re
from datetime import datetime
from random import sample
from urllib.parse import urlparse

from flask import url_for

from . import db
from .constants import (
    VALID_CHARACTER_SEQUENCE, RANDOM_ID_ITERATIONS,
    OUT_OF_LUCK, RANDOM_LINK_LENGTH,
    SHORT_LINK_CHAR_LIMIT, LONG_LINK_CHAR_LIMIT,
    VALID_CHARACTERS_PATTERN, INVALID_URL_FORMAT,
    INVALID_SHORT_LINK, DUPLICATE_SHORT_LINK)
from .error_handlers import ModelValidationError


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(LONG_LINK_CHAR_LIMIT), nullable=False)
    short = db.Column(
        db.String(SHORT_LINK_CHAR_LIMIT), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @classmethod
    def get(cls, field, value):
        return cls.query.filter_by(**{field: value}).first()

    @classmethod
    def get_unique_short_id(cls):
        for _ in range(RANDOM_ID_ITERATIONS):
            random_link = ''.join(
                sample(VALID_CHARACTER_SEQUENCE, RANDOM_LINK_LENGTH))
            if not cls.get('short', random_link):
                return random_link
        raise StopIteration(OUT_OF_LUCK)

    @classmethod
    def create(cls, original, short=None):
        url_map = URLMap(
            original=original,
            short=short or cls.get_unique_short_id())
        db.session.add(url_map)
        db.session.commit()
        return url_map

    @classmethod
    def create_on_validation(cls, url, custom_id=None):
        if not len(url) <= LONG_LINK_CHAR_LIMIT:
            raise ModelValidationError(INVALID_URL_FORMAT.format(url=url))
        url_parts = urlparse(url)
        if not (url_parts.netloc and url_parts.scheme in ('http', 'https')):
            raise ModelValidationError(INVALID_URL_FORMAT.format(url=url))
        if custom_id:
            if not (len(custom_id) < SHORT_LINK_CHAR_LIMIT and
                    re.match(VALID_CHARACTERS_PATTERN, custom_id)):
                raise ModelValidationError(INVALID_SHORT_LINK)
            if URLMap.get('short', custom_id):
                raise ModelValidationError(DUPLICATE_SHORT_LINK.format(
                    short_link=f'"{custom_id}"', end='.'))
        return cls.create(url, custom_id)

    @property
    def fully_qualified_short_link(self):
        return url_for(
            'redirect_to_full_link',
            shortcut=self.short, _external=True)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=self.fully_qualified_short_link
        )
