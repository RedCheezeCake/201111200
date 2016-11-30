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
SERVICE='ListLocaldata470401S'
START_INDEX=str(1)
END_INDEX=str(5)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX)
#print params[31:]

import urlparse

_url='http://openapi.seoul.go.kr:8088/'
url=_url+"/"+KEY+"/"+TYPE+"/"+SERVICE+"/"+START_INDEX+"/"+END_INDEX
#print url

import requests

data=requests.get(url).text
#print data

import lxml
import lxml.etree
import StringIO

#tree=lxml.etree.parse(StringIO.StringIO(data.encode('utf-8')))
tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATMAN')
for node in nodes:
    print node.text