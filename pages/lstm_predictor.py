import streamlit as st
import pickle
import time
import numpy as np
import re
import contractions
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


st.title(" LSTM Sentiment Predictor")

label_map = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}


@st.cache_resource
def load_lstm_model():
    tokenizer = pickle.load(open("models/tokenizer.pkl", "rb"))
    model = load_model("models/lstm_model.keras")
    return model, tokenizer


nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))
negation_words = {"not", "no", "nor", "never"}
stop_words = stop_words - negation_words


def preprocess_text(text):
    if not isinstance(text, str):
        return ""

    text = contractions.fix(text)
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


def predict_lstm(text):
    model, tokenizer = load_lstm_model()

    start = time.time()

    seq = tokenizer.texts_to_sequences([text])

    padded = pad_sequences(
        seq,
        maxlen=100,
        padding="post",
        truncating="post"
    )

    probabilities = model.predict(padded, verbose=0)[0]

    prediction = int(np.argmax(probabilities))
    confidence = float(np.max(probabilities))

    end = time.time()

    return label_map[prediction], confidence, (end - start) * 1000


review = st.text_area("Enter a customer review")

if st.button("Analyze with LSTM", type="primary"):

    if review.strip() == "":
        st.warning("Please enter a review.")
        st.stop()

    review = preprocess_text(review)

    try:
        pred, conf, t = predict_lstm(review)

        st.success(f"Prediction: {pred}")
        st.metric("Confidence", f"{conf:.2%}")
        st.metric("Inference Time", f"{t:.2f} ms")

    except Exception as e:
        st.error("LSTM failed to run.")
        st.code(str(e))