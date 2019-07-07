import csv # to write into csv file
import tweepy
from textblob import TextBlob

# assigning the consumer key
consumer_key =""
consumer_secret = ""
# assigning the token 
access_token = ""
access_token_secret= ""
# creating tweeter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# API 'api' created
api = tweepy.API(auth)
#search function to search the tweets related to given topic
public_tweets = api.search('Education')

'''here create csv file object'''
#open a csv file in write mode or create if file doesnot exist
f= open('tweets.csv','w',newline='') 
#give header names
theeditor = csv.writer(f)

theeditor.writerow(['Tweets','sentiments'])



for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	theeditor.writerow([tweet.text,analysis.sentiment])

