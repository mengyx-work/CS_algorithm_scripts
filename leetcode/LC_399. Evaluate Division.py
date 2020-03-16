from collections import defaultdict
class Solution(object):
    def findQueryRes(self, m, query):
        visited = set()
        queue, target = [(query[0], 1)], query[1]
        while queue:
            next_queue = []
            for char, cur in queue:
                visited.add(char)
                for elem, val in m[char]:
                    if elem == target:
                        return cur * val
                    elif elem not in visited:
                        next_queue.append((elem, cur*val))
            queue = next_queue[:]
        return -1.

    def calcEquation(self, equations, values, queries):
        m = defaultdict(list)
        zeros, known = set(), set()
        for i in range(len(values)):
            a, b = equations[i]
            value = values[i]
            # print(equations[i], a, b)
            known.add(a)
            known.add(b)
            if value == 0:
                zeros.add(a)
            else:
                m[a].append((b, value))
                m[b].append((a, 1/value))
        res = []
        for query in queries:
            a, b = query
            if a not in known or b not in known:
                res.append(-1.)
            elif a in zeros:
                res.append(0.)
            elif a == b:
                res.append(1.)
            else:
                res.append(self.findQueryRes(m, query))
        return res


sol = Solution()
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(sol.calcEquation(equations, values, queries))
