import heapq
class Solution(object):
    def connectSticks(self, sticks):
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            res += x
            res += y
            heapq.heappush(sticks, x+y)
        return res

