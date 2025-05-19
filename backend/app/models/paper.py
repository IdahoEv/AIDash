from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class PaperBase(BaseModel):
    title: str
    authors: List[str]
    abstract: str
    categories: List[str]
    url: Optional[str] = None
    doi: Optional[str] = None

class PaperCreate(PaperBase):
    pass

class Paper(PaperBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True 