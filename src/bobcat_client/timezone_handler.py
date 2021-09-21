from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


class InvalidTimezoneException(Exception):

    def __init__(self, timezone_str):
        super().__init__(f"Timezone: {timezone_str} is not a valid timezone.")


class TimezoneHandler:

    @staticmethod
    def is_valid_timezone(timezone: str):
        try:
            ZoneInfo(key=timezone)
            return True
        except ZoneInfoNotFoundError:
            return False

    @staticmethod
    def convert_timezone(timestamp: str, to_timezone: str, from_timezone: str = 'UTC') -> str:
        original_datetime = datetime.fromisoformat(timestamp.split(" +")[0])
        converted_datetime = original_datetime.replace(tzinfo=ZoneInfo(from_timezone)).astimezone(tz=ZoneInfo(to_timezone))
        # return the timestamp in the same format as the miner: 2021-09-20 04:54:47 +0000 UTC
        return converted_datetime.strftime("%Y-%m-%d %H:%M:%S %z %Z")
