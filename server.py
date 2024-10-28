"""Flask application for emotion detection using NLP."""
from flask import Flask, request, render_template  # Removed unused jsonify import
from EmotionDetection import emotion_detector  # Ensure this imports your emotion detection logic

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Render the index page for the application."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_endpoint():
    """Endpoint to detect emotions from the given text.

    Returns:
        str: A response message containing the emotion analysis result
              or an error message if the input is invalid.
    """
    statement = request.args.get('textToAnalyze', '').strip()
    if len(statement) == 0:
        return "Invalid text! Please try again!", 400

    # Process the emotion detection
    result = emotion_detector(statement)  # Call your emotion detection function

    print(f"Emotion detection result: {result}")  # Debugging line

    # Ensure result contains the expected structure
    response = {
        "output": f"For the given statement, the system response is 'anger': {result['anger']}, "
                  f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
                  f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
                  f"The dominant emotion is {result['dominant_emotion']}.",
        "emotions": {
            "anger": result['anger'],
            "disgust": result['disgust'],
            "fear": result['fear'],
            "joy": result['joy'],
            "sadness": result['sadness'],
            "dominant_emotion": result['dominant_emotion']
        }
    }

    return response["output"]

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
