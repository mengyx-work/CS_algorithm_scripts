import heapq
from collections import defaultdict
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        m = defaultdict(list)
        for s, e, v in flights:
            m[s].append((e, v))
        hq = [(0, src, 0)]
        visited_v, visited_k = {}, {}
        while hq:
            cost, city, cnt = heapq.heappop(hq)
            # print('check city: ', cost, city, cnt, hq)
            if city == dst:
                return cost
            if cnt <= K:
                for other, v in m[city]:
                    # heapq.heappush(hq, (cost+v, other, cnt+1))

                    if other not in visited_v or (cost+v) < visited_v[other] or \
                            other not in visited_k or cnt+1<visited_k[other]:
                        # print('add: ', other)
                        visited_v[other] = cost+v
                        visited_k[other] = cnt+1
                        heapq.heappush(hq, (cost+v, other, cnt+1))
        return -1



sol = Solution()
edges = [[0,1,100],[1,2,100],[0,2,500]]
# print(sol.findCheapestPrice(3, edges, 0, 2, 1))
# assert sol.findCheapestPrice(3, edges, 0, 2, 1) == 200
# assert sol.findCheapestPrice(3, edges, 0, 2, 0) == 500

edges = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
print(sol.findCheapestPrice(5, edges, 0, 2, 2))
# assert sol.findCheapestPrice(5, edges, 0, 2, 2) == 200
