from dataclasses import dataclass, field
from src.bobcat_client.timezone_handler import TimezoneHandler

@dataclass
class Temperature:
    timestamp: str = field(default=None)
    temp0: int = field(default=None)
    temp1: int = field(default=None)
    unit: str = field(default=None)

    def convert_timestamp_timezone(self, to_timezone: str):
        self.timestamp = TimezoneHandler.convert_timezone(timestamp=self.timestamp, to_timezone=to_timezone)

@dataclass
class SyncStatus:
    status: str = field(default=None)
    gap: int = field(default=None)
    miner_height: int = field(default=None)
    blockchain_height: int = field(default=None)
    epoch: int = field(default=None)

