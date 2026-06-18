import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import io


# ============================================================
# PAGE CONFIG
# ============================================================

st.title(" Exploratory Data Analysis")
st.subheader("InsightCart - Customer Reviews Analysis")


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_reviews.csv")


df = load_data()


# ============================================================
# DATASET OVERVIEW
# ============================================================

st.write("### Dataset Preview")
st.dataframe(df.head(), width="stretch")

with st.expander("View Dataset Info"):
    info_df = pd.DataFrame({
        "Column": df.columns,
        "Non-Null Count": df.notnull().sum().values,
        "Missing Values": df.isnull().sum().values,
        "Data Type": df.dtypes.astype(str).values
    })

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Rows", df.shape[0])

    with col2:
        st.metric("Total Columns", df.shape[1])

    with col3:
        st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

    st.write("#### Column Summary")
    st.dataframe(info_df, width="stretch")


with st.expander("View Sentiment Counts"):
    if "Sentiment" in df.columns:
        sentiment_counts_table = df["Sentiment"].value_counts().reset_index()
        sentiment_counts_table.columns = ["Sentiment", "Count"]
        st.dataframe(sentiment_counts_table, width="stretch")
    else:
        st.warning("Column 'Sentiment' not found in dataset.")


st.markdown("---")


# ============================================================
# GRAPH 1: CUSTOMER SENTIMENT DISTRIBUTION
# Notebook equivalent: sns.countplot(x='Sentiment')
# ============================================================

st.write("### Customer Sentiment Distribution")

if "Sentiment" in df.columns:

    sentiment_counts = df["Sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ["Sentiment", "Count"]

    fig_sentiment_bar = px.bar(
        sentiment_counts,
        x="Sentiment",
        y="Count",
        title="Customer Sentiment Distribution",
        text="Count"
    )

    fig_sentiment_bar.update_layout(
        xaxis_title="Sentiment",
        yaxis_title="Count"
    )

    st.plotly_chart(fig_sentiment_bar, width="stretch")

else:
    st.warning("Column 'Sentiment' not found. Cannot create sentiment distribution graph.")


st.markdown("---")


# ============================================================
# GRAPH 2: RATING DISTRIBUTION
# Notebook equivalent: sns.countplot(x='Rating')
# ============================================================

st.write("### Rating Distribution")

if "Rating" in df.columns:

    rating_counts = df["Rating"].value_counts().reset_index()
    rating_counts.columns = ["Rating", "Count"]
    rating_counts = rating_counts.sort_values("Rating")

    fig_rating = px.bar(
        rating_counts,
        x="Rating",
        y="Count",
        title="Rating Distribution",
        text="Count"
    )

    fig_rating.update_layout(
        xaxis_title="Rating",
        yaxis_title="Count"
    )

    st.plotly_chart(fig_rating, width="stretch")

else:
    st.warning("Column 'Rating' not found. Cannot create rating distribution graph.")


st.markdown("---")


# ============================================================
# GRAPH 3: SENTIMENT PERCENTAGE PIE CHART
# Notebook equivalent: df['Sentiment'].value_counts().plot.pie()
# ============================================================

st.write("### Sentiment Percentage")

if "Sentiment" in df.columns:

    sentiment_percentage = df["Sentiment"].value_counts().reset_index()
    sentiment_percentage.columns = ["Sentiment", "Count"]

    fig_sentiment_pie = px.pie(
        sentiment_percentage,
        names="Sentiment",
        values="Count",
        title="Sentiment Percentage",
        hole=0
    )

    fig_sentiment_pie.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    st.plotly_chart(fig_sentiment_pie, width="stretch")

else:
    st.warning("Column 'Sentiment' not found. Cannot create sentiment percentage pie chart.")


st.markdown("---")


# ============================================================
# GRAPH 4: TOP 10 COUNTRIES BY REVIEWS
# Notebook equivalent: fill_between + line plot
# ============================================================

st.write("### Top 10 Countries by Reviews")

if "Country" in df.columns:

    top_countries = df["Country"].value_counts().head(10).reset_index()
    top_countries.columns = ["Country", "Number of Reviews"]

    fig_country = go.Figure()

    fig_country.add_trace(
        go.Scatter(
            x=top_countries["Country"],
            y=top_countries["Number of Reviews"],
            mode="lines+markers",
            fill="tozeroy",
            name="Reviews"
        )
    )

    fig_country.update_layout(
        title="Top 10 Countries by Reviews",
        xaxis_title="Country",
        yaxis_title="Number of Reviews",
        hovermode="x unified"
    )

    st.plotly_chart(fig_country, width="stretch")

else:
    st.warning("Column 'Country' not found. Cannot create top countries graph.")


