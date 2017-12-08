"""
This module demonstrates the representing of graphs in dictionarys.
"""
#!/usr/bin/env python
#representig directed graphs
EX_GRAPH0 = {0: set([1,2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3]), 3: set([0]), 4: set([1]), 5: set([2]), 6: set([])}
EX_GRAPH2 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3,7]), 3: set([7]), 4: set([1]), 5: set([2]), 6: set([]), 7: set([3]), 8: set([1,2]), 9: set([0,3,4,5,6,7])}
def make_complete_graph(num_nodes):
	"""
	Form a complete graph
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

