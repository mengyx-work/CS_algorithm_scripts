from collections import defaultdict
class Solution(object):
    def root(self, idx, i):
        while idx[i] != i:
            idx[i] = idx[idx[i]]
            i = idx[i]
        return i

    def findRedundantConnection(self, edges):
        idx = defaultdict(int)
        for edge in edges:
            st, ed = edge
            if idx[st] == 0:
                idx[st] = st
            if idx[ed] == 0:
                idx[ed] = ed
            st_root = self.root(idx, st)
            ed_root = self.root(idx, ed)
            if st_root == ed_root:
                return edge
            else:
                idx[ed_root] = st_root
        return []

sol  = Solution()
edges = [[1,2], [1,3], [2,3]]
print(sol.findRedundantConnection(edges))