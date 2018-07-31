from django.utils.deprecation import MiddlewareMixin
from marathon_utils.response import JsonErrorResponse
from marathon_utils.exceptions import InvalidQueryParamValueException


class MarathonExceptionsMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, InvalidQueryParamValueException):
            return JsonErrorResponse(exception.error, exception.description)
        else:
            return None