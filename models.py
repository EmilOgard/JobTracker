from dataclasses import dataclass

@dataclass
class Job:
    finn_code: str | None
    title: str
    description: str | None
    company: str
    location: str | None
    url: str | None
    status: str | None
    date_applied: str | None
