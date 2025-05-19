# Tweet scraper using snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd

query = 'AI OR machine learning lang:en'
tweets = []
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) > 100:
        break
    tweets.append([tweet.date, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'Tweet'])
df.to_csv('tweets.csv', index=False)
