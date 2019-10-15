
from collections import defaultdict

class Solution(object):
    def _findDepth(self, curNode, prevNode, neighbors, curDepth):
        if curNode not in neighbors:
            return 0
        if len(neighbors[curNode]) == 1 and neighbors[curNode][0] == prevNode:
            return curDepth + 1
        maxDepth = curDepth
        for node in neighbors[curNode]:
            if node == prevNode:
                continue
            maxDepth = max(maxDepth, self._findDepth(node, curNode, neighbors, curDepth+1))
        return maxDepth

    def findMinHeightTrees(self, n, edges):
        neighbors, resDict = {}, {}
        for i in range(n):
            neighbors[i] = []
        for node1, node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)

        for i in range(n):
            resDict[i] = self._findDepth(i, None, neighbors, 0)

        minHeight = min(resDict.values())
        # print 'minHeight:', minHeight
        res = [root for root in range(n) if resDict[root] == minHeight]
        return res


sol = Solution()
# print sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
assert sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]) ==[1]
assert sol.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]) == [3, 4]
assert sol.findMinHeightTrees(1, []) == [0]






