from typing import Optional
from pydantic import BaseModel


class AIPlanRequest(BaseModel):
    class_name: str
    subject: str
    age: int
    topic: str
    hours: int
    preferences: Optional[str] = None


class AIPlanSchema(BaseModel):
    pass