class NumArray(object):

    def __init__(self, nums):
        self.sumArr,curSum = [], 0
        for num in nums:
            curSum += num
            self.sumArr.append(curSum)

    def sumRange(self, i, j):
        if i == 0:
            sum1 = 0
        else:
            sum1 = self.sumArr[i-1]
        sum2 = self.sumArr[j]
        return sum2 - sum1

# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))