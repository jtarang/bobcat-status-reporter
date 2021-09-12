from dataclasses import dataclass, field


@dataclass
class Temperature:
    timestamp: str = field(init=False)
    temp0: int = field(init=False)
    temp1: int = field(init=False)
    unit: str = field(init=False)
    raw_object: dict = field(repr=False, init=True, default=None)

    def __post_init__(self):
        if self.raw_object is not None:
            self.timestamp = self.raw_object['timestamp']
            self.temp0 = self.raw_object['temp0']
            self.temp1 = self.raw_object['temp1']
            self.unit = self.raw_object['unit']
        del self.raw_object


@dataclass
class SyncStatus:
    status: str = field(init=False)
    gap: int = field(init=False)
    miner_height: int = field(init=False)
    blockchain_height: int = field(init=False)
    raw_object: dict = field(repr=False, init=True, default=None)

    def __post_init__(self):
        if self.raw_object is not None:
            self.status = self.raw_object['status']
            self.gap = self.raw_object['gap']
            self.miner_height = self.raw_object['miner_height']
            self.blockchain_height = self.raw_object['blockchain_height']
        del self.raw_object
