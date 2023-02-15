import re
from http import HTTPStatus

from flask import request, jsonify

from . import app, db
from .error_handlers import InvalidAPIUsage
from .constants import (
    DOESNT_EXIST_MSG, EMPTY_REQUEST_MSG, FIELDS_MISSING_MSG,
    INVALID_URL_FORMAT_MSG, INVALID_SHORT_LINK_MSG, DUPLICATE_SHORT_LINK_MSG)
from .models import URLMap
from .views import get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_full_link(short_id):
    link = URLMap.query.filter_by(short=short_id).first()
    if not link:
        raise InvalidAPIUsage(DOESNT_EXIST_MSG, 404)
    return jsonify({'url': link.original})


@app.route('/api/id/', methods=['POST'])
def create_shortcut():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(EMPTY_REQUEST_MSG)
    if 'url' not in data:
        raise InvalidAPIUsage(FIELDS_MISSING_MSG.format(field='url'))
    if not re.match(r'^https?://.*$', data['url']):
        raise InvalidAPIUsage(INVALID_URL_FORMAT_MSG.format(url=data['url']))
    custom_id = data.get('custom_id')
    if custom_id:
        if not re.match(r'^[a-zA-Z\d]{1,16}$', custom_id):
            raise InvalidAPIUsage(INVALID_SHORT_LINK_MSG)
        if URLMap.query.filter_by(short=custom_id).first() is not None:
            raise InvalidAPIUsage(DUPLICATE_SHORT_LINK_MSG.format(
                short_link=f'"{custom_id}"', end='.'))
    url_map = URLMap()
    url_map.original = data['url']
    url_map.short = custom_id or get_unique_short_id()
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
