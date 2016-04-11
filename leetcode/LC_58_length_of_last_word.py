class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        strs = s.split()
        if(len(strs)==0):
            return 0
        lastWord = strs[len(strs)-1]
        for i in range(len(lastWord)):
            if ord(lastWord[i])>122 or ord(lastWord[i])<65:
                return 0
                break

        return len(lastWord)


solu = Solution()

strs = "the long sent I have use  "

print solu.lengthOfLastWord(strs)
