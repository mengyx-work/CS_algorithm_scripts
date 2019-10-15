class Solution(object):
    def wordFitsPattern(self, word, pattern):
        if len(word) != len(pattern):
            return False
        patternDict = {}
        for i in range(len(pattern)):
            # print patternDict
            if pattern[i] not in patternDict:
                if word[i] in patternDict.values():
                    return False
                patternDict[pattern[i]] = word[i]
                continue
            if patternDict[pattern[i]] != word[i]:
                return False
        return True

    def findAndReplacePattern(self, words, pattern):
        matchedWords = []
        for word in words:
            if self.wordFitsPattern(word, pattern):
                matchedWords.append(word)
        return matchedWords


sol = Solution()
# print sol.wordFitsPattern('ccc', 'abb')

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
print sol.findAndReplacePattern(words, pattern)

