class Solution(object):
    def find132pattern(self, nums):
        c, ak = [], None
        for i in range(len(nums)-1, -1, -1):
            val = nums[i]
            # print(val, ak, c)
            if ak is not None and val < ak:
                return True

            while c and c[-1] < val:
                ak_candidate = c.pop()
                if ak is None:
                    ak = ak_candidate
                else:
                    ak = max(ak, ak_candidate)
            c.append(val)

        return False

sol = Solution()
# nums = [-1, 3, 2, 0]
# assert sol.find132pattern(nums) == True
nums = [-2,1,2,-2,1,2]
print(sol.find132pattern(nums))
