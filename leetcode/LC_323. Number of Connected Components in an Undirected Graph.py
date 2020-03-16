from collections import defaultdict
class Solution(object):
    def root(self, idx, i):
        old_i = i
        while i != idx[i]:
            idx[i] = idx[idx[i]]
            i = idx[i]
        idx[old_i] = i
        return i

    def countComponents(self, n, edges):
        idx = {}
        for i in range(n):
            idx[i] = i

        for st, ed in edges:
            if self.root(idx, st) != self.root(idx, ed):
                idx[self.root(idx, st)] = self.root(idx, ed)

        cnts, roots = 0, set()
        for i in range(len(idx)):
            found_root = self.root(idx, idx[i])
            if found_root not in roots:
                roots.add(found_root)
                cnts += 1
        return cnts

