from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)

from pyspark.sql import Row
Person = Row('name', 'height')
rows = [Person('kim', 170), Person('lee', 175), Person('lim', 180),]
#rowsRdd = sc.parallelize(rows)
#rowsDf = sqlCtx.createDataFrame(rowsRdd)

rowsDF=sqlCtx.createDataFrame(rows)

rowsDF.printSchema()

rowsDF.where(rowsDF.height < 175)\
    .select([rowsDF.name, rowsDF.height]).show()

rowsDF.groupby(rowsDF.height).max().show()