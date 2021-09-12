class InvalidCredentialsFileException(Exception):

    def __init__(self, raw_data):
        super().__init__(f"Data: {raw_data} is not in JSON format")


class CredentialsFileNotFoundError(Exception):

    def __init__(self, file_path: str):
        super().__init__(f"Credentials file `{file_path}` is not found.")
