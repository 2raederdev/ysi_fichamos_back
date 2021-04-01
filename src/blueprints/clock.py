# -*- coding: utf-8 -*-
from http import HTTPStatus

import flask

from src.exceptions.response_exceptions import BadRequestException, UnauthorizedException

clock_bp = flask.Blueprint('clock', __name__, url_prefix='/api/v1/employees/<int:employee_id>/clock')

@clock_bp.route('', methods=['GET'])
def get_all(employee_id):
    pass