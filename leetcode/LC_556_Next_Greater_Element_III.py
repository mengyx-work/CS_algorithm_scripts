class Solution(object):
    def nextGreaterElement(self, n):
        nums = list(str(n))
        for i in range(len(nums)-2, -1, -1):
            cur_num = nums[i]
            max_num, max_index = -1, -1
            for j in range(i+1, len(nums)):
                if nums[j] > cur_num:
                    if max_num == -1 or max_num > nums[j]:
                        max_num = nums[j]
                        max_index = j

            if max_num != -1:
                # print nums[j], max_num, max_index

                leftNums = nums[:i] + [nums[max_index]]
                rightNums = nums[i:]
                rightNums.remove(nums[max_index])
                rightNums.sort()
                resNums = leftNums + rightNums
                res = int(''.join(resNums))
                if res > n and res <= ((1<<31)-1):
                    return res
        return -1

sol = Solution()
print sol.nextGreaterElement(1234)
print sol.nextGreaterElement(230241)