## the directed tree graph uses this reference:
## http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/	
## tree and algorithm is from
## http://www.quora.com/Graph-Theory/What-is-the-difference-between-depth-first-search-and-breadth-first-search-1


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'G']),
         'D': set(['B', 'F']),
         'E': set(['B', 'F']),
         'F': set(['D', 'E']),
				 'G': set(['C'])}

def Depth_First_Search(graph, start):
	Stack = []
	Stack.append(start)
	Visited = set()

	while len(Stack)!=0:
		v = Stack.pop()
		if v not in Visited:
			print 'visit element: ', v
			Visited.add(v)
			for elem in graph[v]:
				Stack.append(elem)
	return Visited

def Spec_Breath_First_Search(graph, start):
	Stack = []
	Visited = set()
	Visited.add(start)
	Stack.append(start)

	while Stack:
		v = Stack.pop()
		for elem in graph[v]:
			if elem not in Visited:
				print 'visit element: ', elem
				Visited.add(elem)
				Stack.append(elem)


def Breath_First_Search(graph, start):
	Stack = []
	Visited = set()
	Visited.add(start)
	Stack.append(start)

	while Stack:
		v = Stack.pop(0)
		for elem in graph[v]:
			if elem not in Visited:
				print 'visit element: ', elem
				Visited.add(elem)
				Stack.append(elem)


#print Depth_First_Search(graph, 'A')
print Breath_First_Search(graph, 'A')
	
