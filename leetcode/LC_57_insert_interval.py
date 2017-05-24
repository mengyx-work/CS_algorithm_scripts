class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        return self.merge(intervals)

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

    '''
    def _find_start_index(self, intervals, value):
        if intervals[-1].end < value or intervals[0].start > value:
            return -1
        lb, ub = 0, len(intervals) - 1
        while(lb + 1 < ub):
            mid = (lb + ub) // 2
            if intervals[mid].start > value:
                ub = mid
            else:
                lb = mid
        if intervals[lb].end < value:
            return ub
        else:
            return lb

    def _find_end_index(self, intervals, value):
        if intervals[-1].end < value or intervals[0].start > value:
            return -1
        lb, ub = 0, len(intervals) - 1
        while(lb + 1 < ub):
            mid = (lb + ub) // 2
            if intervals[mid].end > value:
                ub = mid
            else:
                lb = mid
        if intervals[lb].end < value:
            return ub
        else:
            return lb

    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        start, end = newInterval.start, newInterval.end
        if start > intervals[-1].end:
            return intervals + [newInterval]
        if end < intervals[0].start:
            return [newInterval] + intervals
        start_index = self._find_start_index(intervals, start)
        end_index = self._find_end_index(intervals, end)
        #print start_index, end_index
        if start_index == -1 and end_index != -1:
            return [Interval(start, intervals[end_index].end)] + intervals[(end_index+1):]
        if end_index == -1 and start_index != -1:
            return intervals[:start_index] + [Interval(intervals[start_index].start, end)]
        if end_index == -1 and end_index == -1:
            return [Interval(min(intervals[start_index].start, start), max(intervals[end_index].end, end))]
        return intervals[:start_index] + [Interval(intervals[start_index].start, intervals[end_index].end)] + intervals[(end_index+1):]
        '''


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


sol = Solution()
intervals = [Interval(1, 5)]
res = sol.insert(intervals, Interval(0, 6))
converted_res = [[e.start, e.end] for e in res]
assert converted_res == [[0, 6]]

#'''
intervals = [Interval(1, 5)]
res = sol.insert(intervals, Interval(2, 3))
converted_res = [[e.start, e.end] for e in res]
assert converted_res == [[1, 5]]

intervals = [Interval(1, 5)]
res = sol.insert(intervals, Interval(6, 8))
converted_res = [[e.start, e.end] for e in res]
assert converted_res == [[1, 5], [6, 8]]


#res = sol.insert(intervals, Interval(1, 4))
#converted_res = [[e.start, e.end] for e in res]
#print converted_res

intervals = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]
#print sol._find_start_index(intervals, 6)
#print sol._find_start_index(intervals, 7)

res = sol.insert(intervals, Interval(4, 9))
converted_res = [[e.start, e.end] for e in res]
#print converted_res


#'''

'''
## test the function
intervals = [Interval(3, 5), Interval(6, 8), Interval(9, 11),  Interval(14, 20)]
assert sol._find_end_index(intervals, 10) == 2
assert sol._find_end_index(intervals, 11) == 2
assert sol._find_end_index(intervals, 4) == 0
assert sol._find_end_index(intervals, 7) == 1

assert sol._find_start_index(intervals, 10) == 2
assert sol._find_start_index(intervals, 11) == 2
assert sol._find_start_index(intervals, 4) == 0
assert sol._find_start_index(intervals, 7) == 1
'''
