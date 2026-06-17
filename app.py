import streamlit as st

st.set_page_config(
    page_title="InsightCart",
    page_icon="🛒",
    layout="wide"
)

# Sidebar content only
with st.sidebar:
    st.title("🛒 InsightCart")
    st.caption("E-Commerce Customer Sentiment Analysis")

    st.markdown("---")

    st.success("NLP + Deep Learning Capstone Project")

    st.markdown("---")

    st.info(
        """
**Project Goal**

Analyze Amazon customer reviews and extract meaningful business insights using NLP and Deep Learning.
"""
    )

    st.markdown("---")

    st.caption("Team InsightCart")