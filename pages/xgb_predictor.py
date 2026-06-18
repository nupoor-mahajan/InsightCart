import streamlit as st
import pickle
import time
import numpy as np

from prediction_utils import preprocess_text, label_map


st.title("XGBoost Sentiment Predictor")


@st.cache_resource
def load_model_files():
    model = pickle.load(open("models/xgb_model.pkl", "rb"))
    vectorizer = pickle.load(open("models/tfidf_xgb.pkl", "rb"))
    return model, vectorizer


model, vectorizer = load_model_files()


def predict_sentiment(text):
    start = time.time()

    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]

    confidence = None
    if hasattr(model, "predict_proba"):
        confidence = np.max(model.predict_proba(vec)[0])

    end = time.time()

    return label_map[int(pred)], confidence, (end - start) * 1000


review = st.text_area("Enter a customer review")

if st.button("Analyze with XGBoost", type="primary"):

    if review.strip() == "":
        st.warning("Please enter a review.")
        st.stop()

    cleaned_review = preprocess_text(review)

    try:
        pred, conf, t = predict_sentiment(cleaned_review)

        st.success(f"Prediction: {pred}")

        if conf is not None:
            st.metric("Confidence", f"{conf:.2%}")

        st.metric("Inference Time", f"{t:.2f} ms")

    except Exception as e:
        st.error("XGBoost failed.")
        st.code(str(e))