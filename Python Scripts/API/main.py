from flask import Flask, request
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import random
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


app = Flask(__name__)

def get_tweet(data):
    tweets = data['text']
    labels = data['label']
    labels = labels.replace(["0","1","2","3","4","5"],['sadness','joy','love','anger','fear','surprise'])
    return tweets, labels

def get_sequences(tokenizer, tweets):
    maxlen = 50
    sequences = tokenizer.texts_to_sequences(tweets)
    padded = pad_sequences(sequences, truncating='post' , padding='post', maxlen = maxlen)
    return padded


def get_emotion(msg):

    tweets, labels = get_tweet(train)
    classes = ['joy', 'fear', 'anger', 'sadness', 'love', 'surprise']

    tokenizer = Tokenizer(num_words=10000, oov_token='<UNK>')
    tokenizer.fit_on_texts(tweets)
    tokenizer.texts_to_sequences([tweets[1]])

    class_to_index = dict((c,i) for i, c in enumerate(classes))
    index_to_class = dict((v, k) for k, v in class_to_index.items())

    msg_seq = get_sequences(tokenizer, [msg])

    p = model.predict(msg_seq)[0]
    pred_class = index_to_class[np.argmax(p).astype('uint8')]

    return pred_class

@app.route("/result", methods=["POST","GET"])
def result():
    output = request.get_json()
    if len(output.keys()) <1:
        return {"Status":"BAD response"}
    msg = output['msg']
    
    emotion = {}

    emotion['emotion'] = get_emotion(msg)
    

    return (emotion)

if __name__ == '__main__':
    model = load_model('C:/Users/valsa/OneDrive - The University of the West Indies, St. Augustine/Final Year/ECNG 3020/Iris/Python Scripts/SA_Model_Final_v8')
    train = pd.read_csv("G:\My Drive\AnjanaValsalan_ECNG 3020\Implementation Files\Datasets\ECNG3020_Final_Dataset\ECNG3020_Train_Dataset.csv")
    test = pd.read_csv("G:\My Drive\AnjanaValsalan_ECNG 3020\Implementation Files\Datasets\ECNG3020_Final_Dataset\ECNG3020_Test_Dataset.csv")
    app.run(debug=True,port=2000)