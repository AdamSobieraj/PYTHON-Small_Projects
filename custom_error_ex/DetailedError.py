from dataclasses import dataclass

@dataclass
class DetailedError(Exception):
    error_code: int
    description: str
