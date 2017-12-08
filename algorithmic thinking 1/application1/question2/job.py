#!/usr/bin/env python

import random
def er_graph(num_nodes, pro):
	"""
	Form a er grap
	"""
	graph = {}
	for line in range(0, num_nodes):
		value = set()
		for info in range(0, num_nodes):
			if info != line:
				a = random.uniform(0,1)
				if a < pro:
					value.add(info)
		graph[line] = value
	return graph


def compute_in_degrees(digraph):
	"""
	Calculate in degrees
	"""
	graph = {}
	nodes = digraph.keys()
	for line in nodes:
		value = 0
		for info in nodes:
			if line in digraph[info]:
				value = value + 1
		graph[line] = value
	return graph

def in_degree_distribution(digraph):
	"""
	Computing degree distribution
	"""
	graph = {}
	dict1 = compute_in_degrees(digraph)
	in_degree = dict1.keys()
	for line in in_degree:
		if dict1[line] in graph.keys():
			graph[dict1[line]] = graph[dict1[line]] + 1
		else:
			graph[dict1[line]] = 1
	return graph




input1 = er_graph(10000, 0.5)
output = in_degree_distribution(input1)
with open('10000_0.5.txt','w') as o:
	key = output.keys()
	for i in key:
		o.write("{} {}\n".format(i, output[i]))
