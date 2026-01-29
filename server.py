"""
Flask server for Emotion Detection application.
Provides a web interface to analyze emotions from text input.
"""

# pylint: disable=import-error

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


# pylint: disable=invalid-name
@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotionDetector():
    """
    Handle emotion detection requests.

    Accepts user text input, processes it using the emotion_detector
    function, and renders results on the web page. Displays an error
    message for blank or invalid input.
    """
    if request.method == 'POST':
        text = request.form.get('statement', '').strip()

        if not text:
            return (
                render_template(
                    'index.html',
                    result=None,
                    error_message="Invalid text! Please try again!"
                ),
                400,
            )

        emotions = emotion_detector(text)

        if not emotions.get("dominant_emotion"):
            return render_template(
                'index.html',
                result=None,
                error_message="Invalid text! Please try again!"
            )

        return render_template('index.html', result=emotions)

    return render_template('index.html', result=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
