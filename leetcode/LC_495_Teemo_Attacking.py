class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        new_intervals = []
        for interval in sorted_intervals:
            if len(new_intervals) == 0:
                new_intervals.append(interval)
            else:
                if interval.start > new_intervals[-1].end:
                    new_intervals.append(interval)
                else:
                    cur_interval = new_intervals.pop()
                    new_intervals.append(Interval(min(cur_interval.start, interval.start), max(cur_interval.end, interval.end)))
        return new_intervals

    def findPoisonedDuration(self, timeSeries, duration):
        intervals = []
        for start in timeSeries:
            intervals.append(Interval(start, start+duration))
        clean_intervals = self.merge(intervals)
        tot_time = 0
        for interval in clean_intervals:
            tot_time += (interval.end - interval.start)
        return tot_time

sol = Solution()
assert sol.findPoisonedDuration([1,4], 2) == 4
assert sol.findPoisonedDuration([1,2], 2) == 3
