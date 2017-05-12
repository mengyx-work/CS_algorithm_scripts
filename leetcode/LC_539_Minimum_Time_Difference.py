class Solution(object):
    @staticmethod
    def _time_diff(point1, point2):
        return  60*(int(point2[:2]) - int(point1[:2])) + int(point2[3:]) - int(point1[3:])

    @staticmethod
    def _convert_to_int(timePoint):
        return  60*int(timePoint[:2]) + int(timePoint[3:])

    @staticmethod
    def _add_points(point1, point2, norm=False):
        minutes = int(point1[3:]) + int(point2[3:])
        hours = int(point1[:2]) + int(point2[:2])
        if minutes >= 60:
            minutes -= 60
            hours += 1
        if hours >= 24 and norm:
            hours -= 24
        return '{:02d}:{:02d}'.format(hours, minutes)

    def findMinDifference(self, timePoints):
        sorted_series = sorted(timePoints, key=self._convert_to_int)
        sorted_series.append(self._add_points(sorted_series[0], '24:00'))
        #print sorted_series
        min_diff = None
        for i in range(len(sorted_series) - 1):
            if min_diff is None:
                min_diff = self._time_diff(sorted_series[i], sorted_series[i+1])
            else:
                min_diff = min(min_diff, self._time_diff(sorted_series[i], sorted_series[i+1]))
        return min_diff


sol = Solution()
#print sol._add_points('23:10', '23:50')
series = ["23:59","00:00", "01:03"]
assert sol.findMinDifference(series) == 1
series = ["23:59","00:00"]
assert sol.findMinDifference(series) == 1
