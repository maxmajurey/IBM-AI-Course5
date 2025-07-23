"""
emotion detector function:
    Accepts: str
    Returns: str
"""
from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    renders index page
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    analyzes emotion of input text, identifies if valid input text is presented
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze is None:
        return "Please provide text to analyse.", 400
    emotion_results = emotion_detector(text_to_analyze)

    if emotion_results is None or emotion_results.get('dominant_emotion') is None:
        return "Invalid text! Please try again.", 400
    # Extract individual scores and dominant emotion
    anger = emotion_results['anger']
    disgust = emotion_results['disgust']
    fear = emotion_results['fear']
    joy = emotion_results['joy']
    sadness = emotion_results['sadness']
    dominant_emotion = emotion_results['dominant_emotion']

    # Format the output string as requested
    response_message = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return response_message
if __name__ == "__main__":
    # Ensure Flask runs on localhost:5000
    app.run(host='0.0.0.0', port=5000)
