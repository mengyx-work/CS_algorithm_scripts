class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if len(timeSeries) == 0:
            return 0
        if len(timeSeries) == 1:
            return duration
        prev_start, prev_end = timeSeries[0], timeSeries[0] + duration
        tot_len = 0
        for time in timeSeries[1:]:
            if time <= prev_end:
                prev_end = time + duration
            else:
                tot_len += prev_end - prev_start
                prev_start = time
                prev_end = time + duration
        tot_len += prev_end - prev_start
        return tot_len
sol = Solution()
assert sol.findPoisonedDuration([1, 4], 2) == 4
assert sol.findPoisonedDuration([1, 2], 2) == 3





