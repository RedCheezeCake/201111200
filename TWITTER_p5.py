def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d

import os

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=getKey(keyPath)

import tweepy

auth = tweepy.OAuthHandler(key['CONSUMERKEY'], key['CONSUMERSECRET'])
auth.set_access_token(key['ACCESSTOKEN'],key['ACCESSTOKENSECRET'])
api = tweepy.API(auth)

follower = api.followers()
for i in range(len(follower)):
    print str(follower[i].id) +"\t"+ str(follower[i].screen_name)