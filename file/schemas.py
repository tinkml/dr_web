from datetime import datetime

from pydantic import BaseModel


class File(BaseModel):
    id: int
    uploaded_at: datetime


class CreateFile(BaseModel):
    file_path: str
    file_hash: str

