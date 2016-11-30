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

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='CardBusStatisticsService'
START_INDEX=str(1)
END_INDEX=str(5)
USE_MON=str(201512)
BUS_ROUTE_NO=str(7016)

_url='http://openapi.seoul.go.kr:8088/'
url=_url+"/"+KEY+"/"+TYPE+"/"+SERVICE+"/"+START_INDEX+"/"+END_INDEX+"/"+USE_MON+"/"+BUS_ROUTE_NO

import requests

data=requests.get(url).text
print data