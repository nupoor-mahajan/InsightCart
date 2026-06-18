import streamlit as st
import pandas as pd
import plotly.express as px

st.title(" Dataset Explorer")
st.subheader("Interactive Review Data Exploration")

df = pd.read_csv("data/cleaned_reviews.csv")

st.write("### Raw Dataset")
st.dataframe(df)

st.markdown("---")

st.write("### Filter Data by Sentiment")

sentiments = df["Sentiment"].unique()
selected_sentiment = st.selectbox("Choose Sentiment", sentiments)

filtered_df = df[df["Sentiment"] == selected_sentiment]

st.write(f"Showing {selected_sentiment} reviews")
st.dataframe(filtered_df)

st.markdown("---")

st.write("### Sentiment Distribution")

sentiment_counts = df["Sentiment"].value_counts().reset_index()
sentiment_counts.columns = ["Sentiment", "count"]

fig1 = px.bar(
    sentiment_counts,
    x="Sentiment",
    y="count",
    title="Sentiment Count Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

st.write("### Review Length Insight")

df["review_length"] = df["Review Text"].astype(str).apply(len)

fig2 = px.box(
    df,
    x="Sentiment",
    y="review_length",
    title="Review Length by Sentiment"
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

st.success("Use this page to explore patterns, anomalies, and sentiment behavior in your dataset.")