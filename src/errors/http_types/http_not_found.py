class HttpNotFoundError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.status_code = 404
        self.type = "NotFound"
        self.message = message
