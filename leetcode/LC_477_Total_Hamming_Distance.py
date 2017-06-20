class Solution(object): 
    def totalHammingDistance(self, nums):
        one_counts = {}
        tot_sum, max_len = 0, len(nums)
        for num in nums:
            numStr = list('{:b}'.format(num))
            for i, elem in enumerate(reversed(numStr)):
                if elem == '1':
                    if i not in one_counts:
                        one_counts[i] = 0
                    one_counts[i] += 1
        for count in one_counts.values():
            zero_count = max_len - count
            tot_sum += zero_count * count
        return tot_sum

nums = [4, 14, 2]
sol = Solution()
print sol.totalHammingDistance(nums)


