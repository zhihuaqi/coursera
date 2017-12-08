#!/usr/bin/env python
import urllib2
import random
import time
import math
NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"
def make_complete_graph(num_nodes):
	graph = {}
	for line in range(0, num_nodes):
		value = set()
		for info in range(0, num_nodes):
			if info != line:
				value.add(info)
		graph[line] = value
	return graph
class UPATrial:
	"""
	Simple class to encapsulate optimizated trials for the UPA algorithm	    
	Maintains a list of node numbers with multiple instance of each number.
	The number of instances of each node number are
	in the same proportion as the desired probabilities			    
	Uses random.choice() to select a node number from this list for each trial.
	"""
	def __init__(self, num_nodes):
		"""
		Initialize a UPATrial object corresponding to a 
		complete graph with num_nodes nodes								        
		Note the initial list of node numbers has num_nodes copies of
		each node number
		"""
		self._num_nodes = num_nodes
		self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]
	
	def run_trial(self, num_nodes):
		"""
		Conduct num_nodes trials using by applying random.choice()
		to the list of node numbers
		Updates the list of node numbers so that each node number
		appears in correct ratio
		Returns:
		Set of nodes
		"""
		# compute the neighbors for the newly-created node
		new_node_neighbors = set()
		for _ in range(num_nodes):
			new_node_neighbors.add(random.choice(self._node_numbers))
			# update the list of node numbers so that each node number 
			# appears in the correct ratio
		self._node_numbers.append(self._num_nodes)
		for dummy_idx in range(len(new_node_neighbors)):
			self._node_numbers.append(self._num_nodes)
		self._node_numbers.extend(list(new_node_neighbors))
		#update the number of nodes
		self._num_nodes += 1
		return new_node_neighbors


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
	print "Loaded graph with", len(graph_lines), "nodes"
	answer_graph = {}
	for line in graph_lines:
		neighbors = line.split(' ')
		node = int(neighbors[0])
		answer_graph[node] = set([])
		for neighbor in neighbors[1 : -1]:												answer_graph[node].add(int(neighbor))
	return answer_graph

def er_graph(num_nodes, pro):
	graph = {key: set() for key in xrange(n)}
	for i in xrange(n):
		for j in xrange(n):
			if i ==j:
				continue
			if random.uniform(0,1) < pro:
				graph[i].add(j)
				graph[j].add(i)
	return graph
def upa_graph(num_nodes, m):
	graph = make_complete_graph(m)
	upa = alg_upa_trial.UPATrial(m)
	for i in xrange(m, num_nodes):
		neighbors = upa.run_trial(m)
		graph[i] = neighbors
		for neighbor in neighbors:
			graph[neighbor].add(i)
	return graph

