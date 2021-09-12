class RequestException(Exception):

    def __init__(self, request_obj):
        self.request = request_obj
        super().__init__(f"Host: {self.request.url}:: Response: {self.request.text}")


class ApiKeyException(Exception):

    def __init__(self, api_key: str):
        super().__init__(f"API Key `{api_key}` is not valid or in the correct format")
