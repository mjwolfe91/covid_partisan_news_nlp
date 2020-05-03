import tweepy
from wordcloud import WordCloud
import matplotlib.pyplot as plt

consKey = ""
consSecret = ""
accessKey = ""
accessSecret = ""

auth = tweepy.OAuthHandler(consumer_key=consKey, consumer_secret=consSecret)

auth.set_access_token(accessKey, accessSecret)

api = tweepy.API(auth)
search_term = input("Enter the term to be searched ")
number_of_tweets = int(input("Enter the number of tweets "))

tweets = tweepy.Cursor(api.search, q=search_term, lang="en").items(number_of_tweets)

cloud = ""
for each in tweets:
    cloud = cloud + each.text

cloud = WordCloud(background_color="white").generate(cloud)

plt.imshow(cloud)
plt.axis('off')
plt.show()