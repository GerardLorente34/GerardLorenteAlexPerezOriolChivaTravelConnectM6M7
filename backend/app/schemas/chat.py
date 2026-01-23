import datetime
from pydantic import BaseModel


class ChatMessageResponse(BaseModel):
    id: int
    viaje_id: int
    autor_id: int
    autor_username: str
    contenido: str
    timestamp: datetime.datetime

    class Config:
        from_attributes = True


class SendMessageRequest(BaseModel):
    contenido: str