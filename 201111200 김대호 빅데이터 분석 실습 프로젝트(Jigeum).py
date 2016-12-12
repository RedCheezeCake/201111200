
# coding: utf-8

# In[ ]:

from pymongo import MongoClient

# DB Connection =======================
client = MongoClient('localhost:27017')
db = client.jigeum  #jigeum db 생성 


# In[ ]:

import requests
import re
import urllib
import datetime
import time
from konlpy.tag import Hannanum # for Analyze in description


while (True):
    db.jgTable.update_many({"recent":1},{"$set":{"recent":0}},True)

    # Real-Time Rank part ================================
    data=requests.get('http://www.naver.com/')
    _html = data.text

    item=re.compile('href="http://search.naver.com/(.*?)"')
    items=item.findall(_html)

    resultStr = ''
    cnt=0
    for i in items:
        if i.startswith('search.naver?where=nexearch&amp;query=') :
            cnt+=1        
            if cnt <11 :
                resultStr += i + '\n'

    #data cleaning 1 : extract unicode
    resultStr = resultStr.replace('search.naver?where=nexearch&amp;query=','')
    resultStr = resultStr.replace(';sm=top_lve&amp;ie=utf8','')
    resultStr = resultStr.encode('utf-8')

    #data cleaning 2 : decode 
    resultStr = urllib.unquote(resultStr)
    resultStr = resultStr.replace('+',' ')
    resultStr = resultStr.replace('&amp','')

    # result saving in list
    resultList = resultStr.split('\n')

    # API Searching part  ==============================
    id="XEOUmdxdH8k80PurVLOK"
    key="Pq7gQcPlvA"
    display = 100
    start = 1
    sort = 'date'    

    hannanum = Hannanum()


    for idx in range(10) :

        # Searching Word 
        _searchWord = resultList[idx] 
        _realtimeRank = idx+1
        _time = datetime.datetime.now()

        # User Dictionary 
        faDic = open("c:\Users\Kool\Anaconda2\Lib\site-packages\konlpy\java\data\kE\dic_user.txt",'a') # for write in User Dictionary
        frDic = open("c:\Users\Kool\Anaconda2\Lib\site-packages\konlpy\java\data\kE\dic_user.txt",'r') # for read User Dictionary
        userDic = frDic.read()
        if userDic.find(_searchWord.replace(" ","")) < 0 :
            faDic.write(_searchWord.replace(" ","")+"\tncn\n")
        frDic.close()
        faDic.close()
        
        # create Header
        hdr = {'Host':'openapi.naver.com','User-Agent': 'curl/7.43.0','Accept': '*/*','Content-Type': 'application/xml','X-Naver-Client-Id': id,'X-Naver-Client-Secret': key}

        # create URL
        url='https://openapi.naver.com/v1/search/news.xml?'  # blog ?  news ? 
        url+='query='+_searchWord
        url+='&'
        url+='display='+str(display)
        url+='&'
        url+='start='+str(start)
        url+='&'
        url+='sort='+sort

        # Crawling Query Data
        data=requests.get(url, headers = hdr)

        resultDic = {_searchWord:0}    

        # Analyse Result Dictionary variable       
        _html = data.text
        item=re.compile('<item>(.*?)</item>')
        items=item.findall(_html)
        for i in items:
            description=re.compile('<description>(.*?)</description>')
            desResultStr = ""

            descriptions=description.findall(i)
            for k in descriptions :
                k=k.replace('&lt;b&gt;','')
                k=k.replace('&lt;/b&gt;','')
                k=k.replace('\'','')
                k=k.replace('\"','')
                k=k.replace('&it;','')
                k=k.replace('&gt;','')
                k=k.replace('&amp;','')
                k=k.replace('&apos;','')
                k=k.replace('&quot;','')
                k=k.replace(',','')
                k=k.replace('.','')
                k=k.replace('(',' ')
                k=k.replace(')',' ')
                k=k.replace(')',' ')
                k=k.replace(_searchWord.decode('utf-8'),' ')
                #k=k.replace(_searchWord.decode('utf-8'),_searchWord.replace(' ','').decode('utf-8'))
                k_nouns = hannanum.nouns(k)
                for _k in k_nouns :
                    if len(_k) > 1 :
                        desResultStr += _k+" "
                        if _k in resultDic :
                            resultDic[_k] = resultDic.get(_k)+1
                        else :
                            resultDic[_k] = 1

        # Dictionary -> List
        analyseList = []
        for k in resultDic.keys() :
            analyseList.append([resultDic[k],k])

        #write Analyse Result
        analyseList.sort(reverse=True)

        #db.jgTable.update({"recent":1},{"recent":0})
        for n in range(10):
            _analyseWord = analyseList[n][1]
            _frequency = analyseList[n][0]
            _analyseRank = n
            db.jgTable.insert_one({
                    "realtimeRank": _realtimeRank,
                    "searchWord": _searchWord,
                    "analyseWord": _analyseWord,
                    "frequency": _frequency,
                    "analyseRank": _analyseRank,
                    "time" :{ 
                        "year": _time.year,
                        "month": _time.month,
                        "day": _time.day,
                        "hour": _time.hour,
                        "minute": _time.minute
                    },
                    "recent" : 1
            })

    print str(_time) + " okay.."
    time.sleep(110)



print "\nprogram CLOSE..."

