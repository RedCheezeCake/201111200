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

q = '#seoul'
count = 100
prev_id=None
f=open('_todel3.txt','a')
for i in range(0,20):
    search_result = api.search(q,count=10,since_id=prev_id)
    print len(search_result)
    for i in range(len(search_result)):
        #print str(i),tweet['id'],tweet['user']['name'],tweet['text']
        f.write(str(i)+ "\t"+str(search_result[i].created_at)+"\t"+search_result[i].text.encode('utf-8'))
        f.write("\n")
    #if data["statuses"] == []:
    #    print "end of data"
    #    break
    #else:
    prev_id=int(search_result[i].id)-1
    print prev_id
f.close()

