class RequestException(Exception):

    def __init__(self, request_obj):
        self.request = request_obj
        super().__init__(f"Host: {self.request.url}:: Response: {self.request.text}")


class HostCannotBeReachedException(Exception):

    def __init__(self, host_address):
        super().__init__(f"Host {host_address}: Cannot be reached")
