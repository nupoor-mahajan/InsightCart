import streamlit as st
st.markdown(
    """
    <style>
        h1 {
            font-size: 52px !important;
            font-weight: 800 !important;
        }

        h2, h3 {
            font-size: 32px !important;
            font-weight: 700 !important;
        }

        [data-testid="stMarkdownContainer"] p {
            font-size: 22px !important;
            line-height: 1.7 !important;
        }

        [data-testid="stMarkdownContainer"] li {
            font-size: 22px !important;
            line-height: 1.7 !important;
        }

        [data-testid="stCaptionContainer"] {
            font-size: 18px !important;
        }

        [data-testid="stAlert"] p {
            font-size: 20px !important;
        }

        /* Bigger markdown badges */
        [data-testid="stMarkdownContainer"] span[data-testid="stBadge"] {
            font-size: 20px !important;
            padding: 6px 12px !important;
            border-radius: 10px !important;
        }

        /* Neater card text */
        div[data-testid="stVerticalBlockBorderWrapper"] p {
            font-size: 18px !important;
            line-height: 1.5 !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] h3 {
            font-size: 24px !important;
            margin-bottom: 8px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🛒 InsightCart")
st.subheader("E-Commerce Customer Sentiment Analysis Platform")

st.markdown(
    """
InsightCart is an AI-powered analytics system designed to understand customer sentiment
from e-commerce reviews and convert them into meaningful business insights.
"""
)

st.markdown(
    """
:blue-badge[🔍 NLP] 
:green-badge[📊 EDA] 
:orange-badge[🤖 Machine Learning] 
:violet-badge[🧠 Deep Learning] 
:gray-badge[⚡ Streamlit]
"""
)

st.markdown("---")

st.subheader("Project Modules")

col1, col2, col3 = st.columns(3)

with col1:
    st.badge("Data Explorer", icon="📁", color="blue")
    st.write("View cleaned customer review data and filter reviews by sentiment.")

with col2:
    st.badge("EDA Dashboard", icon="📊", color="green")
    st.write("Analyze sentiment distribution, ratings, review patterns, and countries.")

with col3:
    st.badge("Sentiment Prediction", icon="🤖", color="orange")
    st.write("Predict review sentiment using trained machine learning models.")

st.markdown("---")

st.subheader("Models Used")

model_col1, model_col2, model_col3, model_col4 = st.columns(4)

with model_col1:
    st.badge("Random Forest", icon="🌲", color="green")
    st.caption("Classical ML baseline")

with model_col2:
    st.badge("Tuned RF", icon="⚙️", color="blue")
    st.caption("Hyperparameter optimized model")

with model_col3:
    st.badge("XGBoost", icon="⚡", color="orange")
    st.caption("Boosting-based classifier")

with model_col4:
    st.badge("LSTM", icon="🧠", color="violet")
    st.caption("Deep learning sequence model")

st.markdown("---")

st.subheader("How It Works")

step1, step2, step3, step4 = st.columns(4)

with step1:
    with st.container(border=True):
        st.badge("Step 1", icon="🧹", color="blue")
        st.markdown("### Clean")
        st.write("CSV files containing customer reviews are cleaned, normalized, and prepared for analysis.")

with step2:
    with st.container(border=True):
        st.badge("Step 2", icon="📊", color="green")
        st.markdown("### Analyze")
        st.write("EDA is performed to understand sentiment, ratings, and review patterns.")

with step3:
    with st.container(border=True):
        st.badge("Step 3", icon="🤖", color="orange")
        st.markdown("### Train")
        st.write("Machine learning and deep learning models are trained on processed reviews.")

with step4:
    with st.container(border=True):
        st.badge("Step 4", icon="🚀", color="violet")
        st.markdown("### Predict")
        st.write("New customer reviews are classified into sentiment categories in real time.")
st.markdown("---")

st.subheader("Tech Stack")

st.markdown(
    """
:primary-badge[Python] 
:blue-badge[Streamlit] 
:green-badge[Pandas] 
:orange-badge[Scikit-learn] 
:violet-badge[TensorFlow] 
:gray-badge[XGBoost]
"""
)

st.success("Use the sidebar to explore data, view EDA insights, and test sentiment prediction models.")