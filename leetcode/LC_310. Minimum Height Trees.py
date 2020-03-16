from collections import defaultdict
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        cnnt = defaultdict(list)
        if n == 1:
            return [0]

        for st, ed in edges:
            cnnt[st].append(ed)
            cnnt[ed].append(st)
        leaves = []
        for e in cnnt:
            if len(cnnt[e]) == 1:
                leaves.append(e)
        while n > 2:
            print('leaves: ', leaves)
            n -= len(leaves)
            next_leaves = []
            for e in leaves:
                for d in cnnt[e]:
                    cnnt[d].remove(e)
                    if len(cnnt[d]) == 1:
                        next_leaves.append(d)
            leaves = next_leaves[:]
        return leaves

sol = Solution()
# n = 3
# edges = [[0,1],[0,2]]
# assert sol.findMinHeightTrees(n, edges) == [0]
#
# n = 4
# edges = [[1, 0], [1, 2], [1, 3]]
# assert sol.findMinHeightTrees(n, edges) == [1]

n = 2
edges = [[1, 0]]
print(sol.findMinHeightTrees(n, edges))


# n = 6
# edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
# print(sol.findMinHeightTrees(n, edges))
#
# n = 1
# edges = []
# assert sol.findMinHeightTrees(n, edges) == [0]
