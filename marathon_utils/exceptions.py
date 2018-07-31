
class MarathonException(Exception):
    """Generic marathon exception"""
    pass


class MarathonAPIException(MarathonException):
    """Base exception for API errors"""
    def __init__(self, error, description):
        self.error = error
        self.description = description
        super().__init__("{}: {}".format(error, description))


class InvalidQueryParamValueException(MarathonAPIException):
    """Exception raised when one of the query params has invalid value"""
    def __init__(self, description):
        super().__init__("invalid query param value", description)

