import collections
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        st, ed, res = 0, 0, 0
        cts = collections.defaultdict(int)
        for char in s:
            cts[char] += 1
            while len(cts.keys()) > 2:
                cts[s[st]] -= 1
                if cts[s[st]] == 0:
                    cts.pop(s[st])
                st += 1
            # print(char, st, ed)
            res = max(res, ed-st+1)
            ed += 1
        return res

sol = Solution()
s = 'eceba'
print(sol.lengthOfLongestSubstringTwoDistinct(s))
