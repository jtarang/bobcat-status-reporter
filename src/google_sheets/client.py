from json import loads as json_loads
from json.decoder import JSONDecodeError
from typing import List

import gspread
import pandas
from gspread_dataframe import set_with_dataframe, get_as_dataframe

from src.google_sheets.exceptions import InvalidCredentialsFileException, CredentialsFileNotFoundError


class GoogleSheetsClient:

    def __init__(self, google_sheets_service_account_file_path: str, google_sheets_scopes: List[str] = None):
        self.default_google_sheets_scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        self.google_sheets_scopes = self.default_google_sheets_scopes if google_sheets_scopes is None else google_sheets_scopes
        self.google_sheets_service_account_file_path = google_sheets_service_account_file_path
        self.google_sheets_client = self._create_gspread_client()

    def _create_gspread_client(self) -> gspread.Client:
        """
        Check if the credential file is exists and is valid json.
        Then finally return the client, otherwise throw exceptions
        :return: gspread.auth.service_account
        """
        try:
            with open(self.google_sheets_service_account_file_path, 'r') as credentials:
                try:
                    _raw_data = credentials.read()
                    json_loads(_raw_data)
                    return gspread.service_account(filename=self.google_sheets_service_account_file_path,
                                                   scopes=self.google_sheets_scopes)
                except JSONDecodeError:
                    raise InvalidCredentialsFileException(raw_data=_raw_data)
        except FileNotFoundError:
            raise CredentialsFileNotFoundError(file_path=self.google_sheets_service_account_file_path)

    def read_sheet(self, sheet_id: str):
        return self.google_sheets_client.open(title=sheet_id)

    def write_to_sheet(self, sheet_id: str, data: dict,
                       worksheet_id: int = None, clear_worksheet: bool = False) -> None:
        """
            Should probably break out the dataframe creation in another method
        """
        spread_sheet = self.read_sheet(sheet_id=sheet_id)
        if worksheet_id is None:
            worksheet_id = spread_sheet.sheet1.id
        worksheet = spread_sheet.get_worksheet_by_id(worksheet_id)
        if clear_worksheet:
            worksheet.clear()
        pandas_dataframe = pandas.DataFrame(data=data, index=[[key for key in data.keys()][0]])
        if len(worksheet.col_values(1)) == 0:
            set_with_dataframe(worksheet, dataframe=pandas_dataframe)
        else:
            worksheet.append_rows(pandas_dataframe.values.tolist())
        return None