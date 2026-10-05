class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.status_code = 422
        self.type = "UnprocessableEntity"
        self.message = message
