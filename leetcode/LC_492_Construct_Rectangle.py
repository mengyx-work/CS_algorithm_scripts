import math
class Solution(object):
    def constructRectangle(self, area):
        max_w = math.sqrt(area)
        if max_w == int(max_w):
            return [int(max_w), int(max_w)]
        max_w = int(max_w)
        while max_w >= 1:
            l = 1. * area / max_w
            if int(l) == l:
                return [int(l), max_w]
            else:
                max_w -= 1
sol = Solution()
assert sol.constructRectangle(4) == [2, 2]
assert sol.constructRectangle(13) == [13, 1]





