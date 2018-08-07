from django.utils.deprecation import MiddlewareMixin

from marathon_utils.response import JsonErrorResponse
from marathon_utils.exceptions import MarathonAPIException


class MarathonExceptionsMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, MarathonAPIException):
            return JsonErrorResponse(exception.error, exception.description)
        else:
            return None