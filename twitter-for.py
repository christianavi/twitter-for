import tweepy
from credentials import *

auth = tweepy.OAuthHandler(apikey, apisecretkey) 
auth.set_access_token(accesstoken, accesstokensecret) 

api = tweepy.API(auth)

print ("twitter-for [Version 1.0.1]")
print ("Copyright (c) 2020 christianavi. All rights reserved.")

tweet = input("What's happening? ")

api.update_status(status =(tweet))