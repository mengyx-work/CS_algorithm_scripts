from collections import defaultdict
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        neighborDict = defaultdict(list)
        for node1, node2 in edges:
            neighborDict[node1].append(node2)
            neighborDict[node2].append(node1)
        len0Set, len1Set = set(), set()
        print neighborDict
        for i in xrange(n):
            if len(neighborDict[i]) == 1:
                len1Set.add(neighborDict[i][0])
            if len(neighborDict[i]) == 0:
                len1Set.add(i)
        if len(len0Set) > 0:
            return list(len0Set)
        else:
            return list(len1Set)
sol = Solution()
#assert sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]) ==[1]
#assert sol.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]) == [3, 4]
print sol.findMinHeightTrees(1, [])





