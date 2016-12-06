from pyspark.mllib.stat import Statistics

parallelData = sc.parallelize([1.0, 2.0, 5.0, 4.0, 3.0, 3.3, 5.5])

testResult = Statistics.kolmogorovSmirnovTest(parallelData, "norm", 0, 1)
print(testResult)