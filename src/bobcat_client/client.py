from src.base_http_client.client import BaseHttpClient
from src.bobcat_client.models import SyncStatus, Temperature


class BobcatClient(BaseHttpClient):

    def __init__(self, miner_ip_address: str, scheme: str = 'http'):
        self.miner_ip_address = f'{scheme}://{miner_ip_address}'
        super().__init__(host=self.miner_ip_address)
        self.api_endpoints = {
            "temperature": "/temp.json",
            "sync_status": "/status.json"
        }

    def get_temperature(self) -> Temperature:
        temp_response = self.do_get(api_endpoint=self.api_endpoints['temperature'])
        return Temperature(raw_object=temp_response)

    def get_sync_status(self) -> SyncStatus:
        sync_status = self.do_get(api_endpoint=self.api_endpoints['sync_status'])
        return SyncStatus(raw_object=sync_status)


if __name__ == "__main__":
    miner_ip = "192.168.50.155"
    bobcat_client = BobcatClient(miner_ip_address=miner_ip)
    temp = bobcat_client.get_temperature()
    print()
