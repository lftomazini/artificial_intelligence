import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import itertools

data = np.array([])
centroids = np.array([])
groups = [0]
new_groups = [1]
color_dict = {0: 'red', 1: 'black'}
labels = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']

np.set_printoptions(threshold='nan')
np.set_printoptions(suppress=True)

''' Puts average of column for nan and scales values in range 0 to 1'''
def preprocessing():
	global data
	global max_value

	col_mean = np.nanmean(data, axis=0)
	indexes = np.where(np.isnan(data))
	data[indexes] = np.take(col_mean, indexes[1])
	data = data / data.max(axis=0)

''' Create the clusters based on the closest neighbour'''
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

''' Redefines the centroids based on the new clusters generated'''
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

''' Plots a bidimensional graph of the two attributes'''
def plot_data(x_attribute, y_attribute):
	global data

	fig, ax = plt.subplots()
	ax.set_xlabel(labels[x_attribute])
	ax.set_ylabel(labels[y_attribute])
	ax.scatter(np.array(data[:,x_attribute]),np.array(data[:,y_attribute]), c=map(color_dict.get, np.floor(data[:,-1])), edgecolors = map(color_dict.get, groups), linewidth = 1.5)
	# plt.show()
	plt.savefig('att' + str(x_attribute) + '_x_att' + str(y_attribute))

''' Generates al graphs up to the nth attribute'''
def generate_figures(num_attributes):
	attributes = itertools.combinations(range(1, num_attributes + 1), 2)
	for item in attributes:
		plot_data(item[0], item[1])


if __name__ == "__main__":
	data = np.genfromtxt(sys.argv[1])
	preprocessing()

	''' Assign random initial position for the centroids'''
	centroids = np.random.rand(2, 11)

	''' Repeats the process while there is no convergence'''
	while (groups != new_groups):
		clusters()

	''' Exports results'''
	generate_figures(5)
