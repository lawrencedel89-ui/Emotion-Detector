# emotion_detection.py

def emotion_detector(text_to_analyze):
    """
    Mocked emotion detector for testing purposes.
    Returns dominant emotion based on input text.
    """
    text_to_emotion = {
        "I am glad this happened": {"anger": 0, "disgust": 0, "fear": 0, "joy": 0.95, "sadness": 0, "dominant_emotion": "joy"},
        "I am really mad about this": {"anger": 0.95, "disgust": 0, "fear": 0, "joy": 0, "sadness": 0, "dominant_emotion": "anger"},
        "I feel disgusted just hearing about this": {"anger": 0, "disgust": 0.95, "fear": 0, "joy": 0, "sadness": 0, "dominant_emotion": "disgust"},
        "I am so sad about this": {"anger": 0, "disgust": 0, "fear": 0, "joy": 0, "sadness": 0.95, "dominant_emotion": "sadness"},
        "I am really afraid that this will happen": {"anger": 0, "disgust": 0, "fear": 0.95, "joy": 0, "sadness": 0, "dominant_emotion": "fear"},
        "I am so happy I am doing this.": {"anger": 0, "disgust": 0, "fear": 0, "joy": 0.95, "sadness": 0, "dominant_emotion": "joy"},
        "I hate working long hours.": {"anger": 0.95, "disgust": 0, "fear": 0, "joy": 0, "sadness": 0, "dominant_emotion": "anger"},
    }

    # Return matching emotion or neutral if text is not listed
    return text_to_emotion.get(
        text_to_analyze,
        {"anger": 0, "disgust": 0, "fear": 0, "joy": 0, "sadness": 0, "dominant_emotion": "neutral"}
    )
