#!/usr/bin/env python

import urllib2
def make_complete_graph(num_nodes):
	"""
	Form a complete grap
	"""
	graph = {}
	for line in range(0, num_nodes):
		value = set()
		for info in range(0, num_nodes):
			if info != line:
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



CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
	"""
	Function that loads a graph given the URL
	for a text representation of the graph
	Returns a dictionary that models a graph
	"""
	graph_file = urllib2.urlopen(graph_url)
	graph_text = graph_file.read()
	graph_lines = graph_text.split('\n')
	graph_lines = graph_lines[ : -1]
						    
	print "Loaded graph with", len(graph_lines), "node"
	answer_graph = {}
	for line in graph_lines:
		neighbors = line.split(' ')
		node = int(neighbors[0])
		answer_graph[node] = set([])
		for neighbor in neighbors[1 : -1]:
			answer_graph[node].add(int(neighbor))	
	return answer_graph

input1 = load_graph(CITATION_URL)
output = in_degree_distribution(input1)
with open('','w') as o:
	key = output.keys()
	for i in key:
		o.write("{} {}\n".format(i, output[i]))
