graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


#'''
def dfs(graph, start):
	visited, stack = set(), [start]
	while stack:
		vertex = stack.pop()
		print 'new vertext: ', vertex
		if vertex not in visited:
			visited.add(vertex)
			print 'visited: ', visited
			stack.extend(graph[vertex] - visited)
			print 'stack: ', stack
	return visited
#'''

'''
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
'''

result = dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}
print result
