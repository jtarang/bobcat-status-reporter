from dataclasses import dataclass, field
from src.bobcat_client import MinerState


@dataclass
class Temperature:
    timestamp: str = field(default=None)
    temp0: int = field(default=None)
    temp1: int = field(default=None)
    unit: str = field(default=None)


@dataclass
class SyncStatus:
    status: str = field(default=MinerState.offline)
    gap: int = field(default=None)
    miner_height: int = field(default=None)
    blockchain_height: int = field(default=None)
    epoch: int = field(default=None)

