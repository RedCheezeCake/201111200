path = "c:\Users\Kool\Documents\data\spark_wiki.txt"
lines = sc.textFile(path)
wc = lines\
    .flatMap(lambda x: x.split(' '))
wc.collect()

from operator import add
wc = sc.textFile(path)\
    .flatMap(lambda x: x.split(' '))\
    .map(lambda x: (x.lower().rstrip().lstrip().rstrip(',').rstrip('.'), 1))\
    .reduceByKey(add)

wc.count()

wc.first()

from operator import add
wc = sc.textFile(path)\
    .map(lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower())\
    .map(lambda x:x.split())\
    .map(lambda x:[(i,1) for i in x])

for e in wc.collect():
    print e

documents = sc.textFile(path).map(lambda line: line.split(" "))

from pyspark.mllib.feature import HashingTF

hashingTF = HashingTF()
tf = hashingTF.transform(documents)

tf.collect()