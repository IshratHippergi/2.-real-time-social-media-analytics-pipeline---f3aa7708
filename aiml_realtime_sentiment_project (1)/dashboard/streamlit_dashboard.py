
import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

st.title("Real-Time Social Media Sentiment Dashboard")
query = st.text_input("Enter a topic:", "AI")

# Load tweet data from CSV instead of scraping
df = pd.read_csv('sample_tweets.csv')
tweets = df['content'].tolist()

# Sentiment Analysis
sentiments = {"Positive": 0, "Negative": 0, "Neutral": 0}
for tweet in tweets:
    analysis = TextBlob(tweet)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        sentiments["Positive"] += 1
    elif polarity < 0:
        sentiments["Negative"] += 1
    else:
        sentiments["Neutral"] += 1

# Display pie chart
st.write("### Sentiment Distribution")
plt.figure(figsize=(6, 4))
plt.pie(sentiments.values(), labels=sentiments.keys(), autopct='%1.1f%%')
st.pyplot(plt)
