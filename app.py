
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = analyzer.polarity_scores(str(text))['compound']
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Streamlit page layout
st.set_page_config(page_title="Sentiment Analyzer", layout="wide")
st.title("📊 Social Media Sentiment Analyzer")
st.markdown("Analyze social media posts using VADER sentiment analysis.")

# =======================
# CSV Upload Section
# =======================
uploaded_file = st.file_uploader("Upload CSV file with posts:", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    text_col = st.selectbox("Select the text column:", df.columns)
    
    # Apply sentiment analysis
    df["Sentiment"] = df[text_col].apply(analyze_sentiment)
    df["Sentiment_Score"] = df[text_col].apply(lambda x: analyzer.polarity_scores(str(x))["compound"])
    
    st.subheader("✅ Sample Results")
    st.dataframe(df.head(10))
    
    # Sentiment counts cards
    counts = df["Sentiment"].value_counts()
    col1, col2, col3 = st.columns(3)
    col1.metric("Positive Posts", counts.get("Positive", 0), "😊")
    col2.metric("Neutral Posts", counts.get("Neutral", 0), "😐")
    col3.metric("Negative Posts", counts.get("Negative", 0), "😔")
    
    # Pie chart of sentiment
    st.subheader("📊 Sentiment Distribution")
    fig = px.pie(df, names='Sentiment', title='Sentiment Distribution', color='Sentiment',
                 color_discrete_map={'Positive':'green','Neutral':'blue','Negative':'red'})
    st.plotly_chart(fig, use_container_width=True)
    
    # Download CSV
    csv = df.to_csv(index=False)
    st.download_button("📥 Download Sentiment CSV", csv, "sentiment_result.csv", "text/csv")

# =======================
# Single Text Analysis
# =======================
st.subheader("Or Analyze Single Text:")
user_text = st.text_area("Enter your text here:")
if st.button("Analyze Text"):
    if user_text.strip() != "":
        score = analyzer.polarity_scores(user_text)["compound"]
        sentiment = analyze_sentiment(user_text)
        st.success(f"Sentiment: {sentiment} | Compound Score: {score}")
    else:
        st.warning("Please enter some text to analyze.")
