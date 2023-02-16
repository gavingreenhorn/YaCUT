from datetime import datetime
from random import sample
from urllib.parse import urljoin

from . import db
from .constants import (
    VALID_CHARACTER_SEQUENCE, RANDOM_ID_ITERATIONS,
    OUT_OF_LUCK, BASE_HTTP_ADDRESS)


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(128), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @classmethod
    def get(cls, field, value):
        return cls.query.filter_by(**{field: value}).first()

    @classmethod
    def get_unique_short_id(cls):
        for _ in range(RANDOM_ID_ITERATIONS):
            random_link = ''.join(sample(VALID_CHARACTER_SEQUENCE, 6))
            if not cls.get('original', random_link):
                return random_link
        else:
            raise SystemError(OUT_OF_LUCK)

    @property
    def fully_qualified_short_link(self):
        return urljoin(BASE_HTTP_ADDRESS, self.short)

    def create(self, original, short=None):
        self.original = original
        self.short = short or self.get_unique_short_id()
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=self.fully_qualified_short_link
        )

    def from_dict(self, data):
        for field in ['url', 'custom_id']:
            if field in data:
                setattr(self, field, data[field])
