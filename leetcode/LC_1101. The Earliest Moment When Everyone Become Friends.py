# class Solution(object):
#     def update_parents(self, parents, N):
#         for i in range(N):
#             # print('parents:, ', parents)
#             while parents[i] != parents[parents[i]]:
#                 parents[i] = parents[parents[i]]
#
#     def root_idx(self, parents, idx):
#         while parents[idx] != idx:
#             idx = parents[idx]
#         return idx
#
#     def earliestAcq(self, logs, N):
#         parents = [i for i in range(N)]
#         logs.sort(key=lambda x: x[0])
#         # print('logs: ', logs)
#         for time, i, j in logs:
#             p, q = min(i, j), max(i, j)
#             # parents[self.root_idx(parents, q)] = parents[self.root_idx(parents, p)]
#             # print('before: ', parents)
#             self.update_parents(parents, N)
#             # print('after: ', parents)
#             if len(set(parents)) == 1:
#                 return time
#         return -1

class Solution(object):
    def earliestAcq(self, logs, N):
        root = {x: x for x in range(N)}
        self.groups = N
        logs.sort(key=lambda x: x[0])

        def merge(x, y):
            x, y = find(x), find(y)
            if x != y:
                self.groups -= 1
                root[x] = y

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        for t, x, y in logs:
            merge(x, y)
            if self.groups == 1:
                return t
        return -1





sol = Solution()
logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
N = 6
print(sol.earliestAcq(logs, N))