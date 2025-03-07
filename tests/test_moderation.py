import pytest
from app.moderation import moderate_message

def test_moderate_message():
    test_content = "I hate you!"
    is_flagged, reason, confidence = moderate_message(test_content)
    assert isinstance(is_flagged, bool)
    assert reason in ["harassing/hate", "spam", "explicit", "other"]
    assert 0.0 <= confidence <= 1.0