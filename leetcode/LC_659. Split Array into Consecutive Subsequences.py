import heapq

class Element(object):
    def __init__(self, num, cnt):
        self.num = num
        self.cnt = cnt

    def __eq__(self, other):
        return self.num == other.num and other.cnt == self.cnt

    def __lt__(self, other):
        if self.num == other.num:
            return self.cnt < other.cnt
        else:
            return self.num < other.num


class Solution(object):
    def isPossible(self, nums):
        if len(nums) == 0:
            return False
        hq = []
        for num in nums:
            if len(hq) == 0:
                heapq.heappush(hq, Element(num, 1))
            else:
                if num == hq[0].num:
                    heapq.heappush(hq, Element(num, 1))
                else:
                    while hq and hq[0].num + 1 < num:
                        elem = heapq.heappop(hq)
                        if elem.cnt < 3:
                            return False
                    if hq:
                        elem = heapq.heappop(hq)
                        heapq.heappush(hq, Element(num, elem.cnt + 1))

        while hq:
            elem = heapq.heappop(hq)
            if elem.cnt < 3:
                return False
        return True

sol = Solution()
nums = [1,2,3,4,6,7,8,9,10,11]
assert sol.isPossible(nums) == True

nums = [1,2,3,3,4,4,5,5]
assert sol.isPossible(nums) == True
nums = []
assert sol.isPossible(nums) == False
nums = [1,2]
assert sol.isPossible(nums) == False
nums = [1,2,3,4,4,5]
assert sol.isPossible(nums) == False
nums = [1,2,3,3,4,5]
assert sol.isPossible(nums) == True
