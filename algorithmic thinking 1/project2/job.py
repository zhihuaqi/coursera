"""
This module demonstrates the resilience of a graph.
"""
#!/usr/bin/env python
from collections import deque
#test={0: set([1,4]), 1: set([0,3]), 2: set([]), 3: set([1,4]), 4: set([0,3])}
#test1 = [0,1,2,3,4]
def bfs_visited(ugraph, start_node):
	"""
	Breadth-first search
	"""
	queue = deque()
	visited=set([start_node])
	queue.append(start_node)
	while queue:
		jour = queue.popleft()
		for item in ugraph[jour]:
			if item not in visited:
				visited.add(item)
				queue.append(item)

	return visited

def cc_visited(ugraph):
	"""
	find all the nodes in a connected component
	"""
	remain = set(ugraph.keys())
	connected_component = []
	while remain:
		item = remain.pop()
		visited = bfs_visited(ugraph, item)
		connected_component.append(visited)
		remain = remain - visited
	return connected_component

def largest_cc_size(ugraph):
	"""
	return the size of the largest connected component
	"""
	connected_component = cc_visited(ugraph)
	length = 0
	for item in connected_component:
		if len(item) > length:
			length = len(item)
	return length

def compute_resilience(ugraph, attack_order):
	"""
	compute resilience
	"""
	size_info = []
	size_info.append(largest_cc_size(ugraph))
	for item in attack_order:
		for info in ugraph.keys():
			if item == info:
				del ugraph[item]
			elif item in ugraph[info]:
				ugraph[info].remove(item)
		size_info.append(largest_cc_size(ugraph))
	return size_info
#print compute_resilience(test,test1)
