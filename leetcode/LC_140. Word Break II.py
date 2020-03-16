class Solution(object):
    def wordBreak(self, s, wordDict):
        res = [[] for _ in range(len(s))]
        for word in wordDict:
            if len(word) <= len(s) and s.startswith(word):
                res[len(word)-1].append([word])

        for i in range(1, len(s)):
            # print(i, res)
            results = res[i][:]
            for word in wordDict:
                if i >= len(word) and s[(i-len(word)+1):(i+1)] == word and len(res[i-len(word)]) > 0:
                    for one_res in res[i-len(word)]:
                        cur_res = one_res[:]
                        cur_res.append(word)
                        results.append(cur_res)
                res[i] = results

        return [' '.join(elem) for elem in res[len(s)-1]]

sol = Solution()
s = "catsanddog"
dic = ["cat", "cats", "and", "sand", "dog"]
print(sol.wordBreak(s, dic))

s = "aaaaaaa"
dic = ["aaaa","aa","a"]
print(sol.wordBreak(s, dic))

## ETL test case
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
dic = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]