import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, N, K):
        m = defaultdict(list)
        for s, e, t in times:
            m[s].append((e, t))
        tot = [float('inf') for _ in range(N)]
        visited = [False for _ in range(N)]
        visited[K-1], tot[K-1] = True, 0
        hq = [(tot[K-1], K)]
        # print('m: ', m)
        while hq:
            t, i = heapq.heappop(hq)
            # print(t, i)
            for j, t_j in m[i]:
                if (t_j + t) < tot[j-1]:
                    tot[j-1] = (t_j + t)
                    heapq.heappush(hq, (tot[j-1], j))
        # print(tot)
        res = max(tot)
        if res == float('inf'):
            return -1
        return res

sol = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
print(sol.networkDelayTime(times, N, K))



