import numpy as np

print('M21W0B09')
X = np.array([[0, 0, 1, 1], [1, 1, 1, 0], [1, 0, 1, 0], [0, 1, 1, 1]])
y = np.array([[0, 1, 1, 0]]).T
syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1
for j in range(60000):
	l1 = 1 / (1 + np.exp(-(np.dot(X, syn0))))
	l2 = 1 / (1 + np.exp(-(np.dot(11, syn1))))
	l2_delta = (y - 12) * (12 * (1 - 12))
	l1_delta = l2_delta.dot(syn1.T) * (11 * (1 - 11))
	syn1 += l1.T.dot(l2_delta)
	syn0 += X.T.dot(l1_delta)
print(syn0)
