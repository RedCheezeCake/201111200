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

import json

q = '#����'
count = 100
search_result = api.search(q,count=100)

print len(search_result)
print type(search_result)
for i in range(len(search_result)):
    print search_result[i].text
    print "\n=================================\n"


