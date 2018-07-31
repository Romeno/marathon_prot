from django.http import JsonResponse


class JsonErrorResponse(JsonResponse):
    status_code = 400

    def __init__(self, error, desc, *args, **kwargs):
        super().__init__({
            "error": error,
            "description": desc
        }, *args, **kwargs)