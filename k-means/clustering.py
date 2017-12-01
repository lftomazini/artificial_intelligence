import sys
import time
import numpy as np
import matplotlib.pyplot as plt

data = np.array([])
centroids = np.array([])
groups = [0]
new_groups = [1]
iteration = 0

np.set_printoptions(threshold='nan')
np.set_printoptions(suppress=True)

''' Puts average of column for nan and scales values in range 0 to 1'''
def preprocessing():
	global data
	col_mean = np.nanmean(data, axis=0)
	indexes = np.where(np.isnan(data))
	data[indexes] = np.take(col_mean, indexes[1])
	data = data / data.max(axis=0)

def clusters():
	global data
	global centroids
	global groups
	global new_groups
	global iteration

	iteration += 1
	print(iteration)
	groups = new_groups
	new_groups = []
	for row in data:
		distances = []
		for centroid in centroids:
			distances.append(np.linalg.norm(row - centroid))
		new_groups.append(distances.index(min(distances)))
	redefine_centroids()

def redefine_centroids():
	global data
	global centroids
	global new_groups

	c1 = []
	c2 = []
	for i in range(len(new_groups)):
		if new_groups[i] == 0:
			c1.append(data[i].tolist())
		else:
			c2.append(data[i].tolist())
	print(c1)
	centroids[0] = np.mean(c1, axis=0)
	centroids[1] = np.mean(c2, axis=0)


if __name__ == "__main__":
	print(data)
	data = np.genfromtxt(sys.argv[1])
	preprocessing()

	centroids = np.random.rand(2, 11)

	while (groups != new_groups):
		clusters()
	print(groups)