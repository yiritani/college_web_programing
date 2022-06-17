import statistics
import math


def gini(y):
	m = statistics.mean(y)
	n = len(y)
	a = 2 * m * (n * (n - 1))
	ysum = 0
	for i in range(n):
		for j in range(n):
			ysum = ysum + (math.fabs(y[i] - y[j]))

	return (ysum / a)


y=[1,0,0,0,0,0]
gini(y)