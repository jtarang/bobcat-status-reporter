import typer
from src.bobcat_client.client import BobcatClient
from src.google_sheets.client import GoogleSheetsClient

"""
Usage: report_miner_status.py [OPTIONS] MINER_IP_ADDRESS
                              GOOGLE_SHEETS_CREDENTIALS_FILE_PATH
                              GOOGLE_SHEET_ID
Try 'report_miner_status.py --help' for help.

Error: Missing argument 'MINER_IP_ADDRESS'.

"""

cli = typer.Typer()


@cli.command()
def report_status(miner_ip_address: str, google_sheets_credentials_file_path: str, google_sheet_id: str,
                  worksheet_id: int = None, clear_worksheet: bool = False):
    google_sheets_client = GoogleSheetsClient(
        google_sheets_service_account_file_path=google_sheets_credentials_file_path)
    bobcat_client = BobcatClient(miner_ip_address=miner_ip_address)
    miner_report = {**bobcat_client.get_temperature().__dict__} # **bobcat_client.get_sync_status().__dict__}
    google_sheets_client.write_to_sheet(sheet_id=google_sheet_id, data=miner_report, worksheet_id=worksheet_id,
                                        clear_worksheet=clear_worksheet)
    return None


if __name__ == "__main__":
    cli()
