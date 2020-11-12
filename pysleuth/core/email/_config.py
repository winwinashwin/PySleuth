from dataclasses import dataclass


@dataclass
class Configuration:
    programEmail: str
    adminEmail: str