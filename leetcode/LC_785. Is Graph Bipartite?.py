class Solution(object):
    def isBipartite(self, graph):
        if len(graph) == 0:
            return True
        A, B, visited = set(), set(), set()
        for i in range(len(graph)):
            if len(graph[i]) == 0 or i in visited:
                continue

            is_A, queue = 1, [i]
            while queue:
                next_queue = []
                for i in queue:
                    visited.add(i)
                    # print(i, is_A, A, B)
                    if is_A > 0:
                        if i in B:
                            return False
                        elif i not in A:
                            A.add(i)
                    else:
                        if i in A:
                            return False
                        elif i not in B:
                            B.add(i)
                    next_queue.extend([e for e in graph[i] if e not in visited])
                is_A = -1 * is_A
                queue = next_queue[:]
        return True

sol = Solution()
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
assert sol.isBipartite(graph) == False
graph = [[1,3],[0,2],[1,3],[0,2]]
assert sol.isBipartite(graph) == True


