import sys
from pyspark import SparkContext

if __name__ == "__main__"
	if len(sys.argv) != 2:
		print >> sys.stderr, "Usage: sort <file>"
		exit(-1)
	sc = SparkContext(appName="PythonSort")
	lines = sc.textFile(sys.argv[1], 1)
	sortedCount = lines.flatMap(lambda x: x.split(' ')) \
		.map(lambda x: (int(x), 1))\
		.sortByKey(lambda x: x)

	output = sortedCount.collect()
	for (num, unitcount) in output:
		print num 

	sc.stop()
	