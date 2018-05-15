import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = '0qd3RPPkDEa9Mao5jznxWcpqN'
CONSUMER_SECRET = 'n2U3psMWbCrewnk4tZmMyGknfBDoWGtCToD10uE6yg5C5iDLyA'
OAUTH_TOKEN = '996035830899724291-5rT9IIZGjal59wbSRT4ZvWzg8hUBImT'
OAUTH_TOKEN_SECRET = '8XdNBf1ILtDiuoQr8Mc4mTgHXl84wliJZFa0rxXtMUhEp'
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

LON_WOE_ID = 44418

lon_trends = api.trends_place(LON_WOE_ID)

print(json.dumps(lon_trends, indent=1))