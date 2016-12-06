from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)

from pyspark.sql.functions import rand, randn

df = sqlCtx.range(0, 10)
#df.show()

df.select("id", rand(seed=10).alias("uniform"), randn(seed=27).alias("normal")).show()
#df.describe().show()

df = sqlCtx.range(0, 10).withColumn('rand1', rand(seed=10)).withColumn('rand2', rand(seed=27))
#print df.stat.corr('rand1', 'rand2')
#print df.stat.corr('id', 'id')

names = ["Alice", "Bob", "Mike"]
items = ["milk", "bread", "butter", "apples", "oranges"]
df = sqlCtx.createDataFrame([(names[i % 3], items[i % 5]) for i in range(100)], ["name", "item"])
#df.show(10)

df = sqlCtx.createDataFrame([(1, 2, 3) if i % 2 == 0 else (i, 2 * i, i % 4) for i in range(100)], ["a", "b", "c"])
print df.show(10)