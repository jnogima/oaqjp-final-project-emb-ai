import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the scores from the response
    if response.status_code == 200:
        # Extract set of emotions 
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        # Find the dominant emotion
        emotion_names = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        emotion_values = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        highest_emotion_score = max(emotion_values)
        highest_emotion_score_index = emotion_values.index(highest_emotion_score)
        dominant_emotion = emotion_names[highest_emotion_score_index]
    # If the response status code is 400, set all values to None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    # Return the scores of each emotion and the dominant one
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 
    'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}


