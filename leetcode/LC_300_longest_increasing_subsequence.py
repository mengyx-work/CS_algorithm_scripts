class Solution(object):
    def lengthOfLIS(self, nums):
        size = 0
        min_values = []
        for num in nums:
            i, j = 0, len(min_values)
            while (i!=j):
                mid = i + (j-i) // 2
                if min_values[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            if i == len(min_values):
                min_values.append(num)
            else:
                min_values[i] = num
            size = max(i+1, size)
        return size
