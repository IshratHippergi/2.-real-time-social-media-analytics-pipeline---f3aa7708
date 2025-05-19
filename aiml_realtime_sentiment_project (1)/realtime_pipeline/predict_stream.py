# Real-time sentiment prediction using TextBlob
from textblob import TextBlob

def analyze_sentiment(tweet):
    blob = TextBlob(tweet)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Example
print(analyze_sentiment('AI is amazing!'))
