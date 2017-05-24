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

sol = Solution()
intervals = [Interval(1, 3), Interval(2, 6), Interval(5, 10), Interval(15, 18)]
res = sol.merge(intervals)
assert [[e.start, e.end] for e in res] == [[1, 10], [15, 18]]
intervals = [Interval(7, 8), Interval(3, 5), Interval(1, 3)]
res = sol.merge(intervals)
assert [[e.start, e.end] for e in res]  == [[1, 5], [7, 8]]
'''
intervals = [Interval(12, 16), Interval(3, 5), Interval(1, 2), Interval(6, 7), Interval(8, 10)]
res = sorted(intervals, key=lambda x: x.start)
print [[e.start, e.end] for e in res]
'''
