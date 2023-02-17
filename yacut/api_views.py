from http import HTTPStatus

from flask import request, jsonify

from . import app
from .error_handlers import InvalidAPIUsage
from .constants import DOESNT_EXIST, EMPTY_REQUEST
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
    try:
        return jsonify(
            URLMap.create_on_validation(data).to_dict()), HTTPStatus.CREATED
    except InvalidAPIUsage as exception:
        raise exception
