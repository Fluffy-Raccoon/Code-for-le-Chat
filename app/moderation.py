import requests
from app.config import settings

def moderate_message(message_content: str) -> (bool, str, float):
    """
    Sends the content to an AI model and classifies it.
    """

    # AI prompt
    prompt = f"""
    Classify this message: "{message_content}"
    
    Categories:
    - safe
    - harassing/hate
    - spam
    - explicit
    - other

    Respond as JSON: {{"category": "<category>", "confidence": <confidence>}}
    """

    response = requests.post(
        settings.LLM_API_URL,
        headers={"Authorization": f"Bearer {settings.LLM_API_KEY}"},
        json={"prompt": prompt, "max_tokens": 50}
    )

    if response.status_code != 200:
        return False, "API Error", 0.0

    data = response.json()
    category = data.get("category", "other")
    confidence = float(data.get("confidence", 0.0))

    flagged_categories = ["harassing/hate", "explicit", "spam"]
    is_flagged = (category in flagged_categories) and (confidence >= settings.MODERATION_THRESHOLD)

    return is_flagged, category, confidence