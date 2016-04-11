class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):

        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in xrange(1, len(s)+1):
            for j in xrange(i):
                if s[j:i] in wordDict and dp[j]==True:
                    dp[i] = True

        #return dp[-1]

        ## return all the valid combinations ##
        ## also a valid solution for word break II ##
        seqs = []
        for i in xrange(len(s)+1):
            seqs.append([])
        
        for i in xrange(1, len(s)+1):
            for j in xrange(i):
                if s[j:i] in wordDict:
                    if j==0:
                        seqs[i].append(s[j:i])
                    elif len(seqs[j])!=0:
                        for res in seqs[j]:
                            seqs[i].append(res+' '+s[j:i])

        return seqs[-1]

solut = Solution()
wrdDic = ["cat", "cats", "and", "sand", "dog"]
s= 'catsanddog'
print solut.wordBreak(s, wrdDic)





        
                 

