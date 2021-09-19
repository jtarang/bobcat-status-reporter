from urllib.parse import urljoin

from requests import get as http_get
from requests.exceptions import ConnectionError

from src.base_http_client.exceptions import RequestException, HostCannotBeReachedException


class BaseHttpClient:

    def __init__(self, host: str):
        self.host = host

    def _build_url(self, api_endpoint: str) -> str:
        return urljoin(base=self.host, url=api_endpoint, allow_fragments=False)

    def do_get(self, api_endpoint: str, query_params: dict = None) -> dict:
        request = None
        if query_params is None:
            query_params = {}
        try:
            request = http_get(url=self._build_url(api_endpoint=api_endpoint), params=query_params)
            if request.ok:
                return request.json()
            raise RequestException(request_obj=request)
        except ConnectionError:
            raise HostCannotBeReachedException(f'Miner {self.host}: cannot be reached.')
