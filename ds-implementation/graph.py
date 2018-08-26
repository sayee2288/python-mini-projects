'''This is a simple python implementation of
a graph with breadth first and depth first search
algorithms, without any error or edge case handling'''

graph = {}

def add(graph, vertex=None, edge=[]):
	if vertex in graph.keys():
		old_edge = graph[vertex]
		new_edge = set(zip(old_edge, edge))
		graph[vertex] = new_edge
	else:
		graph[vertex] = edge

def print_graph(graph):
	if len(graph) != 0:
		for x in graph.keys():
			print('{} -> {}' .format(x, graph[x]))

def dfs_path(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return path
	if start not in graph.keys():
		return None
	else:
		for edge in graph[start]:
			if edge not in path:
				new_path = dfs(graph, edge, end, path)
				if new_path: return new_path
	return None

def bfs(graph, start, end):
    visited, queue = [], [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            if vertex in graph.keys():
            	for v in graph[vertex]:
            		if v not in queue:
            			queue.append(v)
    return visited

while True:
    x = int(input('\n Please select an operation: 1. insert 2. Print: 3. exit 4. dfs 5. bfs \n'))
    if x == 1:
        vertex = input('Please enter the data to place in the graph: ')
        edge = [x for x in input('Enter edges: ').split()]
        add(graph, vertex, edge)
    if x == 2:
        print_graph(graph)
    if x == 3:
        break
    if x == 4:
    	start = input('Enter starting node: ')
    	end = input('Enter ending node: ')
    	print(dfs_path(graph, start, end))
    if x == 5:
    	start = input('Enter starting node: ')
    	end = input('Enter ending node: ')
    	print(bfs(graph, start, end))

