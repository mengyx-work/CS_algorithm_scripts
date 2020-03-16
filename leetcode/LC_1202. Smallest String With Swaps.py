from collections import defaultdict
class Solution(object):
    def find_group(self, e, m, visited):
        group = []
        stack = [e]
        while stack:
            e = stack.pop()
            group.append(e)
            for p in m[e]:
                if p not in visited:
                    stack.append(p)
                    visited.add(p)
        return group

    def build_graph(self, pairs):
        elems, m = set(), defaultdict(list)
        for a, b in pairs:
            elems.add(a)
            elems.add(b)
            m[a].append(b)
            m[b].append(a)
        visited = set()
        groups = []
        for elem in elems:
            if elem not in visited:
                visited.add(elem)
                group = self.find_group(elem, m, visited)
                groups.append(sorted(group))
        return groups

    def smallestStringWithSwaps(self, s, pairs):
        groups = self.build_graph(pairs)
        s = list(s)
        # print(groups)
        for group in groups:
            chars = [s[e] for e in group]
            chars.sort()
            for i in range(len(group)):
                s[group[i]] = chars[i]
        return ''.join(s)

sol = Solution()
s = "dcab"
pairs = [[0,3],[1,2],[0,2]]
assert sol.smallestStringWithSwaps(s, pairs) == 'abcd'

s = "dcab"
pairs = [[0,3],[1,2]]
assert sol.smallestStringWithSwaps(s, pairs) == 'bacd'
