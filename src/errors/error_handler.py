from src.views.http_types.http_response import HttpResponse
from .http_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .http_types.http_bad_request import HttpBadRequestError
from .http_types.http_not_found import HttpNotFoundError

def handle_errors(error: Exception):
    if isinstance(error, (HttpNotFoundError, HttpBadRequestError, HttpUnprocessableEntityError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "type": error.type,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "type": "Server Error",
                "detail": str(error)
            }]
        }
    )
