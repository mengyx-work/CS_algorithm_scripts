class Solution(object):
    def nthUglyNumber(self, n):
        primes = [2, 3, 5]
        k = len(primes)
        idx = [0 for _ in range(k)]
        nums = [1]
        while len(nums) < n:
            minArr = []
            for i in range(k):
                minArr.append(primes[i] * nums[idx[i]])
            minVal = min(minArr)
            for i in range(k):
                if minArr[i] == minVal:
                    idx[i] += 1
            # print(nums, idx)
            nums.append(minVal)
        # print(nums)
        return nums[-1]


sol = Solution()
n = 11
print(sol.nthUglyNumber(n))






