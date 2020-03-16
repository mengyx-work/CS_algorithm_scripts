import heapq

class Solution(object):
    def getSkyline(self, buildings):
        hs, res = [], []
        for b in buildings:
            hs.append((b[0], -b[2]))
            hs.append((b[1], b[2]))
        hs.sort()
        hq, pre = [0], 0
        for t, h in hs:
            if h < 0:
                heapq.heappush(hq, h)
            else:
                hq.remove(-h)
                heapq.heapify(hq)
            print(t, h, hq, res)
            cur = hq[0]
            if pre != cur:
                res.append((t, -cur))
                pre = cur
        return res

sol = Solution()
buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
print(sol.getSkyline(buildings))






