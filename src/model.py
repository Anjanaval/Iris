import requests
import json
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

class SA_Model():
    def __init__(self):
        self.api_url="https://sa-model-api.herokuapp.com/v1/models/SA_Model_Final_v8:predict"
        self.classes = ['joy', 'fear', 'anger', 'sadness', 'love', 'surprise']
        self.class_to_index = dict((c,i) for i, c in enumerate(self.classes))
        self.index_to_class = dict((v, k) for k, v in self.class_to_index.items())
        with open('tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)

    def get_sequences(self, msg):
        maxlen = 50
        sequences = self.tokenizer.texts_to_sequences(msg)
        padded = pad_sequences(sequences, truncating='post' , padding='post', maxlen = maxlen)
        return padded
        
    def get_emotion(self, msg):
        msg_seq = self.get_sequences([msg])

        payload = json.dumps({'signature_name': "serving_default", 'instances': msg_seq.tolist()})
        response = requests.post(self.api_url, data=payload, headers={"content_type": "application/json"})

        predictions = json.loads(response.text)
        emotion = self.index_to_class[np.argmax(predictions['predictions'][0]).astype('uint8')]

        return emotion
