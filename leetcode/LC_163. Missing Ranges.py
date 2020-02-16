class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        res = []
        if len(nums) == 0:
            if lower == upper:
                res.append('{}'.format(lower))
            else:
                res.append('{}->{}'.format(lower, upper))
            return res

        if nums[0] > lower:
            if nums[0] - lower > 1:
                res.append('{}->{}'.format(lower, nums[0]-1))
            else:
                res.append('{}'.format(lower))

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] <= 1:
                continue
            elif nums[i+1] - nums[i] == 2:
                res.append('{}'.format(nums[i]+1))
            else:
                res.append('{}->{}'.format(nums[i]+1, nums[i+1]-1))

        if nums[-1] < upper:
            if upper - nums[-1] > 1:
                res.append('{}->{}'.format(nums[-1]+1, upper))
            else:
                res.append('{}'.format(upper))
        return res

sol = Solution()
print(sol.findMissingRanges([5], 2, 10))


