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

    if not text_to_analyse or text_to_analyse.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    try:
        response = requests.post(url, headers=headers, json=input_json)
        if response.status_code == 400:
            # Return dictionary with None values for all keys as requested
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        # Ensure the request was successful before trying to access .text
        response.raise_for_status()
        # Convert the response text into a dictionary
        response_dict = json.loads(response.text)
        # Extract the required set of emotions and their scores
        emotions = response_dict['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        # Create a dictionary of emotion scores to find the dominant one
        emotion_scores = {'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score}
        # Find the dominant emotion (emotion with the highest score)
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        # Return the output in the specified format
        return {'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion}
    except requests.exceptions.RequestException as e:
        # Handle potential errors like network issues, invalid URL, etc.
        print(f"Error during API call: {e}")
        return None
    except json.JSONDecodeError as e:
        # Handle potential errors if the response is not valid JSON
        print(f"Error decoding JSON response: {e}")
        return response.text # Return raw text if JSON decoding fails, for debugging
    except KeyError as e:
        print(f"Error parsing emotion data from response: Missing key {e}")
        print(f"Full API response: {response.text}") # Print full response for debugging missing keys
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# if __name__ == "__main__":
#     # Example usage: The function will run automatically when the script starts
#     sample_text = " I hate working long hours."
#     print(f"Analyzing text: '{sample_text}'")
#     emotion_results = emotion_detector(sample_text)
#     if emotion_results:
#         print ("\n Emotion Detection Results:", emotion_results)
#     else:
#         print("\n Failed to get emotion detection results.")
    
