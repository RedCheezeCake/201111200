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

timeline = api.home_timeline()
print type(timeline)
print len(timeline)

print type(timeline[0])
for key in timeline[0]._json.keys():
    print key, timeline[0]._json[key]