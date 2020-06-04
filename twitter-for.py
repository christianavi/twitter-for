import tweepy
from credentials import *
auth = tweepy.OAuthHandler(apikey, apisecretkey) 
auth.set_access_token(accesstoken, accesstokensecret) 
api = tweepy.API(auth)
print ("Twitter for [Version 1.0.0]")
print ("Copyright (c) 2020 christianavi. All rights reserved.")
tweet = input("What's happening? ")
api.update_status(status =(tweet))