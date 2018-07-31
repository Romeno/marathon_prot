from .exceptions import InvalidQueryParamValueException


def get_uint_query_param(req, param_name, default=None):
    try:
        param = int(req.GET.get(param_name, default))
    except ValueError as e:
        raise InvalidQueryParamValueException("'{}' should be int".format(param_name))

    if param < 0:
        raise InvalidQueryParamValueException("'{}' should not be negative".format(param_name))

    return param
