class Solution(object):
    def nextGreaterElements(self, nums):
        if len(nums) == 0:
            return []
        counts = len(nums)
        results = [-1] * counts
        stack = []
        for i in xrange(2*counts):
            i = i % counts
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                results[index] = nums[i]
            if i < counts:
                stack.append(i)
        return results

    '''
    def nextGreaterElements(self, nums):
        ## ETL solution without any stack to store the decreasing sequence
        results = []
        for i, num in enumerate(nums):
            next_num = None
            for j in xrange(i+1, len(nums)):
                if nums[j] > num:
                    next_num = nums[j]
                    break
            if next_num is None:
                for j in xrange(0, i):
                    if nums[j] > num:
                        next_num = nums[j]
                        break
            if next_num is not None:
                results.append(next_num)
            else:
                results.append(-1)
        return results
    '''

sol = Solution()
print sol.nextGreaterElements([1,2,1])

