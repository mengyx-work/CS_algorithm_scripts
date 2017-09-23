class Solution(object):
    def findNumberOfLIS(self, nums):
        if len(nums) <= 1:
            return len(nums)
        max_len_pairs = [(1, 1)]
        for i in xrange(1, len(nums)):
            cur_max_len, cur_count = 1, 1
            for j in xrange(i, -1, -1):
                if nums[j] < nums[i]:
                    if max_len_pairs[j][0] + 1 > cur_max_len:
                        cur_max_len = max_len_pairs[j][0] + 1
                        cur_count = max_len_pairs[j][1]
                    elif max_len_pairs[j][0] + 1 == cur_max_len:
                        cur_count += max_len_pairs[j][1] 
            max_len_pairs.append((cur_max_len, cur_count))
        max_len, counts = max_len_pairs[0][0], max_len_pairs[0][1]
        for pair in max_len_pairs[1:]:
            if pair[0] > max_len:
                max_len = pair[0]
                counts = pair[1]
            elif pair[0] == max_len:
                counts += pair[1]
        return counts



sol = Solution()
nums = [1,3,5,4,7]
assert sol.findNumberOfLIS(nums) == 2
nums = [2,2,2,2,2]
assert sol.findNumberOfLIS(nums) == 5



