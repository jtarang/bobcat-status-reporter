from src.base_http_client.client import BaseHttpClient
from src.bobcat_client.models import SyncStatus, Temperature
from src.base_http_client.exceptions import HostCannotBeReachedException


class BobcatClient(BaseHttpClient):

    def __init__(self, miner_ip_address: str, scheme: str = 'http'):
        self.miner_ip_address = f'{scheme}://{miner_ip_address}'
        super().__init__(host=self.miner_ip_address)
        self.api_endpoints = {
            "temperature": "/temp.json",
            "sync_status": "/status.json"
        }

    def get_temperature(self) -> Temperature:
        try:
            # take the response and pass it to the Temperature model directly
            return Temperature(**self.do_get(api_endpoint=self.api_endpoints['temperature']))
        except HostCannotBeReachedException:
            return Temperature()

    def get_sync_status(self) -> SyncStatus:
        try:
            # take the response and pass it to the SyncStatus model directly
            return SyncStatus(**self.do_get(api_endpoint=self.api_endpoints['sync_status']))
        except HostCannotBeReachedException:
            return SyncStatus()


if __name__ == "__main__":
    miner_ip = "192.168.50.155"
    bobcat_client = BobcatClient(miner_ip_address=miner_ip)
    status = bobcat_client.get_sync_status()
    temp = bobcat_client.get_temperature()
    print()
