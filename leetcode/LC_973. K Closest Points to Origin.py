# class Solution(object):
#     def kClosest(self, points, K):
#         res = sorted(points, key=lambda x: x[0]*x[0]+x[1]*x[1])
#         return res[:K]

import heapq

class Solution(object):
    def kClosest(self, points, K):
        pool = []
        for point in points:
            dis = point[0]*point[0]+point[1]*point[1]
            if len(pool) < K:
                pool.append((-dis, point))
                if len(pool) == K:
                    heapq.heapify(pool)
            elif pool[0][0] < -dis:
                    heapq.heapreplace(pool, (-dis, point))

        return [elem[1] for elem in pool]




sol = Solution()
points = [[3,3],[5,-1],[-2,4]]
K = 2
print(sol.kClosest(points, K))
