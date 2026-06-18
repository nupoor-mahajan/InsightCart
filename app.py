import streamlit as st

st.set_page_config(
    page_title="InsightCart",
    page_icon="🛒",
    layout="wide"
)

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            font-size: 20px;
        }

        section[data-testid="stSidebar"] * {
            font-size: 20px !important;
        }

        section[data-testid="stSidebarNav"] li {
            padding: 8px 0px;
        }

        section[data-testid="stSidebarNav"] a {
            font-size: 20px !important;
            font-weight: 500;
        }
    </style>
    """,
    unsafe_allow_html=True
)

home = st.Page("pages/home.py", title="Home")
dataset_explorer = st.Page("pages/dataset_explorer.py", title="Data" )
eda_dashboard = st.Page("pages/eda_dashboard.py", title="EDA" )
lstm_predictor = st.Page("pages/lstm_predictor.py", title="LSTM Predictor" )
rf_predictor = st.Page("pages/random_forest_predictor.py", title="Random Forest Predictor")
tuned_rf_predictor = st.Page("pages/tuned_rf_predictor.py", title="Tuned Random Forest Predictor" )
xgb_predictor = st.Page("pages/xgb_predictor.py", title="XGBoost Predictor" )

with st.sidebar:
    pg = st.navigation(
        [home,dataset_explorer, eda_dashboard, lstm_predictor, rf_predictor, tuned_rf_predictor, xgb_predictor],
        position="sidebar"
    )


pg.run()