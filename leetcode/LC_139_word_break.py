# class Solution(object):
#     def _wordBreak(self, s, idx, wordDict):
#         if idx == len(s):
#             return True
#         # print(s[idx:])
#         for word in wordDict:
#             if (len(s)-idx) >= len(word) and s[idx:].startswith(word):
#                 if self._wordBreak(s, idx+len(word), wordDict):
#                     return True
#         return False
#
#     def wordBreak(self, s, wordDict):
#         return self._wordBreak(s, 0, wordDict)


class Solution(object):
    def wordBreak(self, s, wordDict):
        res = [False for _ in range(len(s))]
        for word in wordDict:
            if len(word) <= len(s) and s.startswith(word):
                res[len(word)-1] = True

        for i in range(1, len(s)):
            # print(i, res)
            if res[i] is True:
                continue
            for word in wordDict:
                if i >= len(word) and s[(i-len(word)+1):(i+1)] == word and res[i-len(word)]:
                    # print(i, word)
                    res[i] = True
                    break
        # print(res)
        return res[len(s)-1]


sol = Solution()
s = "catsanddog"
dic = ["cat", "cats", "and", "sand", "dog"]
assert sol.wordBreak(s, dic) == True

## ETL case
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
dic = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
assert sol.wordBreak(s, dic) == False

s = "catsandog"
dic = ["cats","dog","sand","and","cat"]
assert sol.wordBreak(s, dic) == False

s = "dog"
dic = ["cat", "cats", "and", "sand", "dog"]
assert sol.wordBreak(s, dic) == True

s = "aaaaaaa"
dic = ["aaaa","aa","a"]
assert sol.wordBreak(s, dic) == True

#s= 'aa'
#dic = ['aa', 'a']

s = "ab"
dic = ["a","b"]
assert sol.wordBreak(s, dic) == True
