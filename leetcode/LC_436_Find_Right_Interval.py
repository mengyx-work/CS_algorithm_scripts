import bisect
## Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def find_upper_index(self, target, nums):
        lb, ub = 0, len(nums) - 1
        while(lb + 1 < ub):
            mid = lb + (ub - lb) / 2
            if nums[mid] > target:
                ub = mid
            else:
                lb = mid
        if nums[ub] == target or nums[lb] == target:
            return target
        if nums[ub] < target:
            return -1
        return nums[ub]

    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        starts = {-1 : -1}
        for index, interval in zip(range(len(intervals)), intervals):
            if interval.start not in starts:
                starts[interval.start] = index
        idx = {}
        sorted_starts = sorted(starts.keys())
        for i, elem in enumerate(sorted_starts):
            idx[i] = starts[elem]
            
        result = []
        for interval in intervals:
            #value = self.find_upper_index(interval.end, sorted_starts)
            #result.append(starts[value])
            pos = bisect.bisect_left(sorted_starts, interval.end)
            if pos == len(sorted_starts):
                result.append(-1)
            else:
                result.append(idx[pos])
        return result

def build_intervals(elems):
    intervals = []
    for elem in elems:
        intervals.append(Interval(elem[0], elem[1]))
    return intervals

elems = [ [3,4], [2,3], [1,2] ]
res = [-1, 0, 1]
sol = Solution()
intervals = build_intervals(elems)
#assert sol.findRightInterval(intervals) == res
print sol.findRightInterval(intervals)

elems = [ [1,2] ]
res = [-1]
intervals = build_intervals(elems)
assert sol.findRightInterval(intervals) == res

