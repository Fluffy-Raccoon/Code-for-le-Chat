from pydantic import BaseModel

class IncomingMessage(BaseModel):
    forum_id: str
    user_id: str
    user_name: str
    content: str
    timestamp: float

class ModerationResponse(BaseModel):
    is_flagged: bool
    reason: str
    confidence: float