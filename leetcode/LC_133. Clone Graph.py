# """
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
# """

class Solution(object):
    ### BFS
    def cloneGraph(self, node):
        m = {node: Node(node.val)}
        stack = [node]
        while len(stack) > 0:
            e = stack.pop()
            for other_node in e.neighbors:
                if other_node not in m:
                    m[other_node] = Node(other_node.val)
                    stack.append(other_node)
                e.neighbors.append(m[other_node])
        return m[node]


class Solution(object):
    m = {}
    def cloneGraph(self, node):
        ### DFS
        if node is None:
            return None
        if node not in self.m:
            self.m[node] = Node(node.val)
            for other in node.neighbors:
                self.m[node].neighbors.append(self.cloneGraph(other))
        return self.m[node]


