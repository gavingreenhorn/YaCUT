import re
from http import HTTPStatus
from urllib.parse import urlparse

from flask import request, jsonify

from . import app
from .error_handlers import InvalidAPIUsage
from .constants import (
    DOESNT_EXIST, EMPTY_REQUEST, FIELDS_MISSING, VALID_CHARACTERS_PATTERN,
    INVALID_URL_FORMAT, INVALID_SHORT_LINK, DUPLICATE_SHORT_LINK)
from .models import URLMap


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_full_link(short_id):
    link = URLMap.get('short', short_id)
    if not link:
        raise InvalidAPIUsage(DOESNT_EXIST, 404)
    return jsonify({'url': link.original})


@app.route('/api/id/', methods=['POST'])
def create_shortcut():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(EMPTY_REQUEST)
    if 'url' not in data:
        raise InvalidAPIUsage(FIELDS_MISSING.format(field='url'))
    url_parts = urlparse(data['url'])
    if not (url_parts.netloc and url_parts.scheme in ('http', 'https')):
        raise InvalidAPIUsage(INVALID_URL_FORMAT.format(url=data['url']))
    custom_id = data.get('custom_id')
    if custom_id:
        if not (re.match(VALID_CHARACTERS_PATTERN, custom_id) and
                len(custom_id) < 16):
            raise InvalidAPIUsage(INVALID_SHORT_LINK)
        if URLMap.get('short', custom_id):
            raise InvalidAPIUsage(DUPLICATE_SHORT_LINK.format(
                short_link=f'"{custom_id}"', end='.'))
    url_map = URLMap()
    url_map.create(data['url'], custom_id)
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
