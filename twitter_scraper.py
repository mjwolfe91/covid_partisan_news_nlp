import tweepy
import json

f = open('twitter_auth.json')
auth_dict = json.loads(f.read())
ACCESS_TOKEN = auth_dict['ACCESS_TOKEN']
ACCESS_SECRET = auth_dict['ACCESS_SECRET']
CONSUMER_KEY = auth_dict['CONSUMER_KEY']
CONSUMER_SECRET = auth_dict['CONSUMER_SECRET']

auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
auth.set_access_token(key=ACCESS_TOKEN, secret=ACCESS_SECRET)

api = tweepy.API(auth)

raw_search = api.search(q="(covid%20OR%20coronavirus)%20since%3A2020-03-15")

print(raw_search)