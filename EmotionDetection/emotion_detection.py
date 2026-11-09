import requests
import json
def emotion_detector(text_to_analyze):
	url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
	headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
	input_json = { "raw_document": { "text": text_to_analyze } }

	response = requests.post(
		url,
		json=input_json,
		headers=headers
	)
	response_dict = json.loads(response.text)
	emotions = response_dict['emotionPredictions'][0]['emotion']
	anger = emotions['anger']
	disgust = emotions['disgust']
	fear = emotions['fear']
	joy = emotions['joy']
	sadness = emotions['sadness']
	dominant_emotion = max(emotions, key=emotions.get)
	sorted_keys = sorted(emotions, key=emotions.get, reverse=True)
	results = {}
	for emotion_name in sorted_keys:
   		 results[emotion_name] = emotions[emotion_name]
	results['dominant_emotion'] = dominant_emotion
	return results
