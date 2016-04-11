class Solution:
# @param s, a string
# @param wordDict, a set<string>
# @return a string[]
    def wordBreak(self, s, wordDict):
        size = len(s)
        ans = []
        for i in range(size):
            ans.append([])

        dp = [False] * size

        for i in range(size):
            for j in range(i+1, size+1):
                if s[i:j] not in wordDict:
                    continue
                if i == 0 or (dp[i-1] and i>0):
                    dp[j-1] = True

        print 'the dp: ', dp

        if not dp[-1]:
            return []

        for i in range(size):
            for j in range(i+1, size+1):
                if s[i:j] not in wordDict:
                    continue
                if i == 0 or (dp[i-1] and i>0):
                    dp[j-1] = True
                    if i == 0:
                        ans[j-1] = [s[i:j]]
                    else:
                        for tmpAns in ans[i-1]:
                            ans[j-1].append(tmpAns+' '+s[i:j])
        return ans[-1]





solut = Solution()
s = "catsanddog"
dic = ["cat", "cats", "and", "sand", "dog"]
s = "aaaaaaa"
dic = ["aaaa","aa","a"]

#s= 'aa'
#dic = ['aa', 'a']

#s = "ab"
#dic = ["a","b"]
print solut.wordBreak(s, dic)
