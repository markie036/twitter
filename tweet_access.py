import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter

CONSUMER_KEY = '0qd3RPPkDEa9Mao5jznxWcpqN'
CONSUMER_SECRET = 'n2U3psMWbCrewnk4tZmMyGknfBDoWGtCToD10uE6yg5C5iDLyA'
OAUTH_TOKEN = '996035830899724291-5rT9IIZGjal59wbSRT4ZvWzg8hUBImT'
OAUTH_TOKEN_SECRET = '8XdNBf1ILtDiuoQr8Mc4mTgHXl84wliJZFa0rxXtMUhEp'
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 50
query = 'Weather'

#Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)] # a list comprehension

status_texts = [status._json['text'] for status in results]

screen_names = [ status._json['user']['screen_name']
                    for status in results
                        for mention in status._json['entities']['user_mentions'] ]
                        
hashtags = [hashtag['text']
                    for status in results
                        for hashtag in status._json['entities']['hashtags'] ]
                        
words = [ word
                    for text in status_texts
                        for word in text.split() ]
                        
for entry in [screen_names, hashtags, words]:
        counter = Counter(entry)
        print(counter.most_common()[:10]) # the top 10 results

    