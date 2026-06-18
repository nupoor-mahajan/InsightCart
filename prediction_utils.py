import re
import contractions
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))
negation_words = {"not", "no", "nor", "never"}
stop_words = stop_words - negation_words


label_map = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}


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