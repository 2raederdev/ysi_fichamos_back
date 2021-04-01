# -*- coding: utf-8 -*-
from http import HTTPStatus

import flask

from src.exceptions.response_exceptions import BadRequestException, UnauthorizedException

employees_bp = flask.Blueprint('employees', __name__, url_prefix='/api/v1/employees')

@employees_bp.route('', methods=['GET'])
def get_all():
    return '''
        Buenos días sensei!!!
        <br><br>
        Ya está corriendo el servicio... ahora tengo que crear una BD y conectarlo!!!
        <br><br>
        A tope con el sábado!!!
    ''', HTTPStatus.OK.value


@employees_bp.route('/<employee_id>', methods=['GET'])
def get_one(employee_id):
    return f'Hola, soy el employee {employee_id}', HTTPStatus.OK.value