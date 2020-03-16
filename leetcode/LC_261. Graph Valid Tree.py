class Solution(object):
    def root(self, idx, i):
        while i != idx[i]:
            idx[i] = idx[idx[i]]
            i = idx[i]
        return i

    def validTree(self, n, edges):
        idx = [i for i in range(n)]
        for n1, n2 in edges:
            g1 = self.root(idx, n1)
            g2 = self.root(idx, n2)
            if g1 == g2:
                return False
            idx[g1] = g2
        if len(edges) == (n-1):
            return True
        return False



sol = Solution()

edges = [[2,0],[2,1]]
assert sol.validTree(3, edges) == True

edges = [[0,1], [1,2], [2,3], [1,3]]
assert sol.validTree(5, edges) == False

edges = [[1,0]]
# print(sol.validTree(2, edges))
assert sol.validTree(2, edges) == True

edges = [[0,1], [0,2], [0,3], [1,4]]
assert sol.validTree(5, edges) == True







