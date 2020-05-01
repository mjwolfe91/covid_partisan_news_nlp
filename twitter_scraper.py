import tweepy

auth = tweepy.OAuthHandler(consumer_key='get from David', consumer_secret='get from David')
auth.set_access_token(key='get from David', secret='get from David')

api = tweepy.API(auth)

raw_search = api.search(q="(covid%20OR%20coronavirus)%20since%3A2020-03-15")

print(raw_search)