# -*- coding: utf-8 -*-
from http import HTTPStatus

class ResponseBaseException(Exception):
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR.value

    def __init__(self, message: str = None, status_code: int = None, payload=None):
        Exception.__init__(self)
        if status_code is not None:
            self.status_code = status_code

        if message is None:
            self.message = HTTPStatus(self.status_code).name
        else:
            self.message = message

        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class PermanentRedirectException(ResponseBaseException):
    status_code = HTTPStatus.PERMANENT_REDIRECT.value

    def __init__(self, message=None, payload=None):
        ResponseBaseException.__init__(self, message, self.status_code, payload)


class BadRequestException(ResponseBaseException):
    status_code = HTTPStatus.BAD_REQUEST.value

    def __init__(self, message=None, payload=None):
        ResponseBaseException.__init__(self, message, self.status_code, payload)


class UnauthorizedException(ResponseBaseException):
    status_code = HTTPStatus.UNAUTHORIZED.value

    def __init__(self, message=None, payload=None):
        ResponseBaseException.__init__(self, message, self.status_code, payload)


class ForbiddenException(ResponseBaseException):
    status_code = HTTPStatus.FORBIDDEN.value

    def __init__(self, message=None, payload=None):
        ResponseBaseException.__init__(self, message, self.status_code, payload)


class NotFoundException(ResponseBaseException):
    status_code = HTTPStatus.NOT_FOUND.value

    def __init__(self, message=None, payload=None):
        ResponseBaseException.__init__(self, message, self.status_code, payload)


class ConflictException(ResponseBaseException):
    status_code = HTTPStatus.CONFLICT.value

    def __init__(self, message=None, payload=None):
        ResponseBaseException.__init__(self, message, self.status_code, payload)


class UnprocessableEntityException(ResponseBaseException):
    status_code = HTTPStatus.UNPROCESSABLE_ENTITY.value

    def __init__(self, message=None, payload=None):
        ResponseBaseException.__init__(self, message, self.status_code, payload)


class TooManyRequestsException(ResponseBaseException):
    status_code = HTTPStatus.TOO_MANY_REQUESTS.value

    def __init__(self, message=None, payload=None):
        ResponseBaseException.__init__(self, message, self.status_code, payload)


class InternalServerErrorException(ResponseBaseException):
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR.value

    def __init__(self, message=None, payload=None):
        ResponseBaseException.__init__(self, message, self.status_code, payload)


class NotImplementedException(ResponseBaseException):
    status_code = HTTPStatus.NOT_IMPLEMENTED.value

    def __init__(self, message=None, payload=None):
        ResponseBaseException.__init__(self, message, self.status_code, payload)