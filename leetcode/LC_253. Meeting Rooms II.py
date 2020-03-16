import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])
        hq, res = [], 0
        for interval in intervals:
            if len(hq) > 0:
                end = heapq.heappop(hq)
                if end > interval[0]:
                    heapq.heappush(hq, end)
            heapq.heappush(hq, interval[1])
            # print(interval, hq)
            res = max(res, len(hq))
        return res

sol = Solution()
intervals = [[0, 30],[5, 10],[15, 20]]
# print(sol.minMeetingRooms(intervals))
assert sol.minMeetingRooms(intervals) == 2
intervals = [[7,10],[2,4]]
assert sol.minMeetingRooms(intervals) == 1
