from http import HTTPStatus

from flask import request, jsonify

from . import app
from .error_handlers import ModelValidationError, InvalidAPIUsage
from .constants import DOESNT_EXIST, EMPTY_REQUEST, FIELDS_MISSING
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
    try:
        return (
            jsonify(URLMap.create_on_validation(
                data['url'], data.get('custom_id')).to_dict()),
            HTTPStatus.CREATED)
    except ModelValidationError as error:
        raise InvalidAPIUsage(message=error.message)
