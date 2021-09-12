from src.bobcat_client.client import BobcatClient
from src.google_sheets.client import GoogleSheetsClient


def report_status(miner_ip_address: str, google_sheets_credentials_file_path: str, google_sheet_id: str,
                  worksheet_id: int = None, clear_worksheet: bool = False):
    google_sheets_client = GoogleSheetsClient(
        google_sheets_service_account_file_path=google_sheets_credentials_file_path)
    bobcat_client = BobcatClient(miner_ip_address=miner_ip_address)
    miner_report = {**bobcat_client.get_temperature().__dict__, **bobcat_client.get_sync_status().__dict__}
    google_sheets_client.write_to_sheet(sheet_id=google_sheet_id, data=miner_report, worksheet_id=worksheet_id, clear_worksheet=clear_worksheet)
    return None


if __name__ == "__main__":
    miner_ip_address = "192.168.50.155"
    google_sheets_worksheets_id = "BobcatMinerReport"
    google_sheets_credentials_file = "./.credentials/bobcat-miner-service-account.json"
    clear_worksheet = False
    report_status(miner_ip_address=miner_ip_address, google_sheets_credentials_file_path=google_sheets_credentials_file,
                  google_sheet_id=google_sheets_worksheets_id, clear_worksheet=clear_worksheet)
