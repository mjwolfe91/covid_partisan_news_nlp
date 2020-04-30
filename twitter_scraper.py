import twitter

api = twitter.Api(consumer_key='coming soon...',
                  consumer_secret='coming soon...',
                  access_token_key='coming soon...',
                  access_token_secret='coming soon...',
                  sleep_on_rate_limit=True)

raw_search = api.GetSearch(
    raw_query="q=(covid%20OR%20coronavirus)%20since%3A2020-03-15")

print(raw_search)