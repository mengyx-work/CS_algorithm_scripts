class Solution(object):
    '''
    the longest common substring/subsequence
    followes the same DP logics:
    1. the max_len[i][j] represents the max length of common
    substring/subsequence from str1[:i+1] and str2[:j+1]
    2. when compare the str1[i] and str2[j]:
        if str1[i] == str2[j]:
            max_len[i][j] = max_len[i-1][j-1] + 1
        else
            max_len[i][j] = max(max_len[i][j-1], max_len[i-1][j])
    3. the special case is when i==0 or j==0.
    '''
    def longest_commmon_subsequence(self, str1, str2):
        str1_chars, str2_chars = list(str1), list(str2)
        if len(str1_chars) == 0 or len(str2_chars) == 0:
            return 0
        max_len = [[0] * len(str2_chars)] * len(str1_chars)
        tot_max_len = 0
        for i, str1_char in enumerate(str1_chars):
            for j, str2_char in enumerate(str2_chars):
                if str1_char == str2_char:
                    if i == 0 or j == 0:
                        max_len[i][j] = 1
                    else:
                        max_len[i][j] = max_len[i-1][j-1] + 1
                else:
                    if j == 0 or j == 0:
                        continue
                    else:
                        max_len[i][j] = max(max_len[i-1][j], max_len[i][j-1])
                print i, j, max_len[i][j]
                tot_max_len = max(tot_max_len, max_len[i][j])
        return tot_max_len

sol = Solution()
str1 = 'adcdda'
str2 = 'aeda'
print sol.longest_commmon_subsequence(str1, str2)
