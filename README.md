# InsightCart - E-Commerce Customer Sentiment Analysis

## Overview

InsightCart is an NLP-powered sentiment analysis platform designed to analyze e-commerce customer reviews and classify them into **Positive**, **Negative**, and **Neutral** sentiments.

The project combines **Natural Language Processing**, **Machine Learning**, **Deep Learning**, and **Interactive Data Visualization** to help understand customer opinions, product perception, rating behavior, and review patterns through a Streamlit dashboard.

The platform supports dataset exploration, exploratory data analysis, and real-time sentiment prediction using multiple trained models.

Live App: https://aicw-insightcart.streamlit.app/

---

## Features

### Dataset Explorer

* Interactive customer review dataset viewer
* Sentiment-based filtering
* Raw dataset preview
* Sentiment distribution visualization
* Review length analysis by sentiment

### Exploratory Data Analysis

* Customer sentiment distribution
* Rating distribution
* Sentiment percentage analysis
* Top countries by review count
* Dataset summary and column information
* Interactive Plotly visualizations

### Sentiment Prediction

InsightCart provides separate prediction screens for each trained model:

* Random Forest
* Hyperparameter Tuned Random Forest
* XGBoost
* LSTM Deep Learning Model

Each model page allows the user to enter a customer review and receive:

* Predicted sentiment
* Confidence score
* Inference time

### NLP Preprocessing

* Text lowercasing
* Contraction expansion
* Punctuation and number removal
* Stopword removal
* Negation word preservation
* Lemmatization
* TF-IDF feature extraction for classical ML models
* Tokenization and sequence padding for LSTM

---

## Models Used

### Random Forest

A classical machine learning baseline model trained using TF-IDF features.

### Hyperparameter Tuned Random Forest

An optimized Random Forest model using tuned parameters for improved performance.

### XGBoost

A gradient boosting model trained on TF-IDF features for strong classification performance.

### LSTM

A deep learning sequence model trained using tokenized customer reviews.

---

## Technology Stack

### Programming Language

* Python 3.11

### Libraries and Frameworks

* Streamlit
* Pandas
* NumPy
* Plotly
* Scikit-learn
* XGBoost
* TensorFlow / Keras
* NLTK
* Contractions
* Matplotlib
* Seaborn

---

## Project Structure

```text
InsightCart/
│
├── app.py
├── home.py
├── prediction_utils.py
├── requirements.txt
├── pyproject.toml
├── .python-version
├── README.md
│
├── data/
│   ├── cleaned_reviews.csv
│   ├── eda_reviews.csv
│   └── processed_reviews.csv
│
├── models/
│   ├── random_forest.pkl
│   ├── hypertuned_random_forest.pkl
│   ├── xgb_model.pkl
│   ├── lstm_model.keras
│   ├── tfidf.pkl
│   ├── tfidf_xgb.pkl
│   └── tokenizer.pkl
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_data_preprocessing.ipynb
│   ├── 04_Model-1_Training.ipynb
│   ├── 05_Model-2_Training.ipynb
│   ├── 06_Model-3_XGBoost.ipynb
│   └── 07_Model-4_LSTM.ipynb
│
└── pages/
    ├── home.py
    ├── dataset_explorer.py
    ├── eda_dashboard.py
    ├── random_forest_predictor.py
    ├── tuned_rf_predictor.py
    ├── xgb_predictor.py
    └── lstm_predictor.py
```

---

## Workflow

1. Load customer review dataset
2. Clean and prepare raw review data
3. Perform exploratory data analysis
4. Preprocess review text using NLP techniques
5. Convert text into numerical features
6. Train machine learning and deep learning models
7. Evaluate model performance
8. Save trained models and vectorizers
9. Build Streamlit dashboard
10. Deploy the application for interactive sentiment prediction

---

## Installation

Clone the repository:

```bash
git clone https://github.com/nupoor-mahajan/InsightCart.git
cd InsightCart
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

For Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Using uv

If using `uv`, create the environment and install dependencies with:

```bash
uv venv .venv --python 3.11
.venv\Scripts\Activate.ps1
uv pip install -r requirements.txt --link-mode=copy
```

Run the app:

```bash
python -m streamlit run app.py
```

---

## Deployment

The project is deployed using Streamlit Community Cloud.

Deployment URL:

https://aicw-insightcart.streamlit.app/

The deployment uses:

```text
requirements.txt
.python-version
app.py
pages/
models/
data/
```

---

## Team Members

### Nupoor Mahajan

GitHub: https://github.com/nupoor-mahajan

Responsibilities:

* XG-Boost Model Training
* LSTM Model Training
* Repository management
* Streamlit Deployement

### Akshata Naik

GitHub: https://github.com/NaikAkshata30

Responsibilities:

* Data cleaning
* Exploratory data analysis
* Random Forest Model Training
* PPT and Documentation

### Hansa Gusaiwal

GitHub: https://github.com/hansagusaiwal

Responsibilities:

* NLP Model and Data Preprocessing
* Hyperparameter tuned Random Forest Model Training
* Documentation

---

## Repository

Project Repository:

https://github.com/nupoor-mahajan/InsightCart

---

## Future Enhancements

* Aspect-based sentiment analysis
* Multi-language sentiment analysis
* Product recommendation system
* Real-time review monitoring
* Transformer-based sentiment models such as BERT
* Advanced business intelligence dashboard

---

## License

This project is developed for academic and educational purposes as part of a Capstone Project in AICW by Edunet, sponsored by Microsoft and SAP.

---

## Acknowledgements

* Amazon Reviews Dataset
* Kaggle
* Streamlit
* TensorFlow
* Scikit-learn
* XGBoost
* NLTK
* Open Source Community
