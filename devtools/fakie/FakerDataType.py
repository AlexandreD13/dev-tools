from dataclasses import dataclass


@dataclass
class FakerDataType:
    name: str
    clean_name: str
    description: str
    additional: []