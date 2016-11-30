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

import requests
import re
KEY=str(key['dataseoul'])
TYPE='json'
SERVICE='RealtimeWeatherStation'
START_INDEX=str(1)
END_INDEX=str(5)
STN_NM=u'Áß±¸'

_url='http://openapi.seoul.go.kr:8088/'
url=_url+"/"+KEY+"/"+TYPE+"/"+SERVICE+"/"+START_INDEX+"/"+END_INDEX+"/"+STN_NM

import requests

data=requests.get(url).text
print data