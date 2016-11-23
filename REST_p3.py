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
SERVICE='SearchSTNBySubwayLineService'
START_INDEX=str(1)
END_INDEX=str(10)
LINE_NUM=str(2)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)

import urlparse
_url='http://openAPI.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
print url

import requests
data=requests.get(url).text

import lxml
import lxml.etree
import StringIO

#tree=lxml.etree.parse(StringIO.StringIO(data.encode('utf-8')))
tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATION_NM')
for node in nodes:
    print node.text