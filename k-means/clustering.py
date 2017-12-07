import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

data = np.array([])
centroids = np.array([])
groups = [0]
new_groups = [1]
color_dict = {0: 'red', 1: 'black'}

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

	groups = new_groups
	new_groups = []
	for row in data:
		distances = []
		for centroid in centroids:
			distances.append(np.linalg.norm(row - centroid))
		new_groups.append(distances.index(min(distances)))
	redefine_centroids()

def plot_data():
	global data

	fig, ax = plt.subplots()
	ax.scatter(np.array(data[:,4]),np.array(data[:,6]), c=map(color_dict.get, np.floor(data[:,-1])), edgecolors = map(color_dict.get, groups), linewidth = 1.5)
	plt.show()

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
	centroids[0] = np.mean(c1, axis=0)
	centroids[1] = np.mean(c2, axis=0)


if __name__ == "__main__":
	data = np.genfromtxt(sys.argv[1])
	preprocessing()

	centroids = np.random.rand(2, 11)

	while (groups != new_groups):
		clusters()
	plot_data()