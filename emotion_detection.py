import requests
import json
def emotion_detector(text_to_analyse):
    """
    Analyzes the emotion of the given text using the Watson NLP Emotion Predict function.
    Args:
        text_to_analyse (str): The text to be analyzed for emotions.
    Returns:
        str: The text attribute of the response object from the Emotion Detection function,
             which contains the emotion prediction results.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    try:
        response = requests.post(url, headers=headers, json=input_json)
        # Ensure the request was successful before trying to access .text
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        # Handle potential errors like network issues, invalid URL, etc.
        print(f"Error during API call: {e}")
        return None
    except json.JSONDecodeError as e:
        # Handle potential errors if the response is not valid JSON
        print(f"Error decoding JSON response: {e}")
        return response.text # Return raw text if JSON decoding fails, for debugging
if __name__ == "__main__":
    # Example usage: The function will run automatically when the script starts
    sample_text = "I love this new technology."
    print(f"Analyzing text: '{sample_text}'")
    emotion_results = emotion_detector(sample_text)
    if emotion_results is not None:
        print ("\n Emotion Detection Results:", emotion_results)
    else:
        print("\n Failed to get emotion detection results.")