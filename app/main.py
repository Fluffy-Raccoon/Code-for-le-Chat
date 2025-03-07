from fastapi import FastAPI
from app.models import IncomingMessage, ModerationResponse
from app.moderation import moderate_message

app = FastAPI()  # This is the FastAPI app instance

@app.get("/")
def read_root():
    return {"status": "Moderator service is running"}

@app.post("/moderate", response_model=ModerationResponse)
def moderate_inbound_message(message: IncomingMessage):
    """
    Receives a forum message, checks if it should be flagged, and returns the result.
    """
    is_flagged, reason, confidence = moderate_message(message.content)
    return ModerationResponse(
        is_flagged=is_flagged,
        reason=reason,
        confidence=confidence
    )