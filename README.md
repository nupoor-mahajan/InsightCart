# InsightCart - E-Commerce Customer Sentiment Analysis

## Overview

InsightCart is an NLP-powered sentiment analysis platform designed to analyze Amazon product reviews and extract meaningful customer insights. The project leverages Natural Language Processing (NLP), Deep Learning, and Data Analytics techniques to classify customer reviews into Positive, Negative, and Neutral sentiments while providing interactive visualizations and business intelligence through a Streamlit dashboard.

The system helps businesses understand customer opinions, identify common issues, monitor product perception, and make data-driven decisions based on customer feedback.

---

## Features

### Dataset Exploration

* Interactive dataset viewer
* Review filtering and search
* Statistical summary of reviews

### Exploratory Data Analysis (EDA)

* Sentiment distribution analysis
* Rating distribution visualization
* Review length analysis
* Word frequency analysis
* Positive and Negative word clouds
* Correlation and trend analysis

### NLP Preprocessing

* Text cleaning
* Lowercasing
* Stopword removal
* Tokenization
* Lemmatization/Stemming
* Feature engineering

### Deep Learning Sentiment Classification

* RNN/LSTM-based sentiment model
* Review sentiment prediction
* Confidence score generation
* Model evaluation metrics

### Business Insights

* Customer sentiment trends
* Common positive feedback analysis
* Frequent complaint identification
* Product performance insights

### Interactive Dashboard

* Streamlit-powered web application
* User review sentiment prediction
* Data visualization dashboard
* Business analytics section

---

## Technology Stack

### Programming Language

* Python

### Libraries and Frameworks

* Pandas
* NumPy
* Matplotlib
* Seaborn
* NLTK
* Scikit-Learn
* TensorFlow / Keras
* WordCloud
* Streamlit

### Dataset

Amazon Reviews Dataset

---

## Project Structure

```text
InsightCart/
│
├── data/
│   ├── raw_dataset.csv
│   └── processed_dataset.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_text_preprocessing.ipynb
│   └── 04_model_training.ipynb
│
├── models/
│   ├── sentiment_model.h5
│   └── tokenizer.pkl
│
├── src/
│   ├── data_preprocessing.py
│   ├── eda.py
│   ├── model.py
│   └── prediction.py
│
├── pages/
│   ├── Home.py
│   ├── Dataset_Explorer.py
│   ├── EDA_Dashboard.py
│   ├── Sentiment_Predictor.py
│   └── Business_Insights.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Workflow

1. Load Amazon Review Dataset
2. Perform Data Cleaning
3. Execute Text Preprocessing
4. Conduct Exploratory Data Analysis
5. Train RNN/LSTM Sentiment Model
6. Evaluate Model Performance
7. Deploy Interactive Streamlit Dashboard
8. Generate Business Insights

---

## Installation

Clone the repository:

```bash
git clone https://github.com/nupoor-mahajan/InsightCart.git
cd InsightCart
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

## Future Enhancements

* Multi-language sentiment analysis
* Aspect-based sentiment analysis
* Product recommendation system
* Real-time review monitoring
* Transformer-based models (BERT)
* Deployment on cloud platforms

---

## Team Members

### Nupoor Mahajan

GitHub: https://github.com/nupoor-mahajan

Responsibilities:

* NLP Pipeline Development
* Model Training & Evaluation
* Repository Management

### Akshata Naik

GitHub: https://github.com/NaikAkshata30

Responsibilities:

* Data Cleaning
* Exploratory Data Analysis
* Business Insights Generation

### Hansa Gusaiwal

GitHub: https://github.com/hansagusaiwal

Responsibilities:

* Streamlit Dashboard Development
* UI Integration
* Deployment & Documentation

---

## Repository

Project Repository:
https://github.com/nupoor-mahajan/InsightCart

---

## License

This project is developed for academic and educational purposes as part of a Capstone Project in AICW by Edunet sponsered by Microsoft and SAP.

---

## Acknowledgements

* Amazon Reviews Dataset
* Kaggle
* Streamlit
* TensorFlow
* Scikit-Learn
* NLTK
* Open Source Community
