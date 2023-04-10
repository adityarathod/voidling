from typing import Optional
from pydantic import BaseModel


class QAAnswer(BaseModel):
    answer: Optional[str]
    confidence: float
