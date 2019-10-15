import collections
class Solution(object):
    def findAnagrams(self, s, p):
        dict1 = collections.defaultdict(int)
        dict2 = collections.defaultdict(int)
        for elem in p:
            dict1[elem] += 1
        for elem in s[:len(p)]:
            dict2[elem] += 1
        i, j = 0, len(p)
        ans = []
        while j < len(s):
            if dict1 == dict2:
                ans.append(i)
            # print(i, j, dict2)
            dict2[s[j]] = dict2.get(s[j], 0) + 1
            dict2[s[i]] -= 1
            if dict2[s[i]] < 1:
                _ = dict2.pop(s[i])
            i += 1
            j += 1

        if dict1 == dict2:
            ans.append(i)
        return ans

sol = Solution()
s = "cbaebabacd"
p = "abc"
print(sol.findAnagrams(s, p))
