class Solution(object):
    def increasingTriplet(self, nums):
        i1, i2 = None, None
        for num in nums:
            if i2 is not None and num > i2:
                return True

            if i1 is None:
                i1 = num
            else:
                i1 = min(i1, num)

            if i1 is not None and num > i1:
                if i2 is None:
                    i2 = num
                else:
                    i2 = min(i2, num)
            # print(num, i1, i2)
        return False

sol = Solution()
# nums = [2,1,5,0,3,4]
# assert sol.increasingTriplet(nums) == True
nums = [1,0,0,0,-1,0,0,0,0,0,0,100000000]
print(sol.increasingTriplet(nums))
