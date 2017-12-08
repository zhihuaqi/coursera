#!/usr/bin/env python
import urllib2
import random
import timeit
import math
import project2 as module2
##########################################
#Provided code

def copy_graph(graph):
	new_graph = {}
	for node in graph:
		new_graph[node] = set(graph[node])
	return new_graph

def remove_node(ugraph, node):
	for neighbor in ugraph[node]:
		ugraph[neighbor].remove(node)
	del ugraph[node]

def targeted_order(ugraph):
	new_graph = copy_graph(ugraph)
	order = []
	while len(new_graph) > 0:
		max_degree = -1
		for node in new_graph:
			if len(new_graph[node]) > max_degree:
				max_degree = len(new_graph[node])
				max_degree_node = node
		neighbors = new_graph[max_degree_node]
		new_graph.pop(max_degree_node)
		for neighbor in neighbors:
			new_graph[neighbor].remove(max_degree_node)

		order.append(max_degree_node)
	return order

def fast_targeted_order(ugraph):
	ugraph = copy_graph(ugraph)
	N = len(ugraph)
	degree_sets = [set()] * N
	for node, neighbors in ugraph.iteritems():
		degree = len(neighbors)
		degree_sets[degree].add(node)
	order = []
	for k in range(N-1, -1, -1):
		while degree_sets[k]:
			u = degree_sets[k].pop()
			for neighbor in ugraph[u]:
				d = len(ugraph[neighbor])
				degree_sets[d].remove(neighbor)
				degree_sets[d-1].add(neighbor)
			order.append(u)
			remove_node(ugraph, u)
	return order

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

def er_graph(n, pro):
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
	upa = UPATrial(m)
	for i in xrange(m, num_nodes):
		neighbors = upa.run_trial(m)
		graph[i] = neighbors
		for neighbor in neighbors:
			graph[neighbor].add(i)
	return graph

def random_order(graph):
	choices = graph.keys()
	random.shuffle(choices)
	return choices

def question_one():
	graph_network = load_graph(NETWORK_URL)
	N = len(graph_network)
	graph_er = er_graph(N, 0.004)
	graph_upa = upa_graph(N, 3)
	nt_order = random_order(graph_network)
	er_order = random_order(graph_er)
	upa_order = random_order(graph_upa)
	network_res = module2.compute_resilience(graph_network, nt_order)
	er_res = module2.compute_resilience(graph_er, er_order)
	upa_res = module2.compute_resilience(graph_upa, upa_order)
	with open('network_res.txt', 'w') as o1, open('er_res.txt', 'w') as o2, open('upa_res.txt', 'w') as o3:
		for i in range(0,1240):
			o1.write("{} {}\n".format(i, network_res[i]))
			o2.write("{} {}\n".format(i, er_res[i]))
			o3.write("{} {}\n".format(i, upa_res[i]))

#question_one()
def measure_targeted_order(n,m,func):
	graph = upa_graph(n, m)
	return timeit.timeit(lambda: func(graph), number=1)

def question_three():
	xs = range(10,1000,10)
	m = 5
	ys_targeted = [measure_targeted_order(n,m,targeted_order) for n in xs]
	ys_fast_targeted = [measure_targeted_order(n,m,fast_targeted_order) for n in xs]
	with open ('time_for_targeted_and_fast_order','w') as o:
		n = 0
		for i in xs:
			o.write("{} {} {}\n".format(i, ys_targeted[n], ys_fast_targeted[n]))
			n += 1


#question_three()

def question_four():
	graph_network = load_graph(NETWORK_URL)
	N = len(graph_network)
	graph_er = er_graph(N, 0.004)
	graph_upa = upa_graph(N, 3)
	nt_order = targeted_order(graph_network)
	er_order = targeted_order(graph_er)
	upa_order = targeted_order(graph_upa)
	network_res = module2.compute_resilience(graph_network, nt_order)
	er_res = module2.compute_resilience(graph_er, er_order)
	upa_res = module2.compute_resilience(graph_upa, upa_order)
	with open('network_targeted_res.txt', 'w') as o1, open('er_targeted_res.txt', 'w') as o2, open('upa_targeted_res.txt', 'w') as o3:
		for i in range(0,1240):
			o1.write("{} {}\n".format(i, network_res[i]))
			o2.write("{} {}\n".format(i, er_res[i]))
			o3.write("{} {}\n".format(i, upa_res[i]))

question_four()
