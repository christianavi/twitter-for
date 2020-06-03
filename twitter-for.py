import tweepy
auth = tweepy.OAuthHandler("api-key", "api-secret-key") 
auth.set_access_token("access-token", "access-token-secret") 
api = tweepy.API(auth)
print ("Twitter for [Version 1.0.0]")
print ("Copyright (c) 2020 Warm Bananas. All rights reserved.")
tweet = input("What's happening? ")
api.update_status(status =(tweet))

