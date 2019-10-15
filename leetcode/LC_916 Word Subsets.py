class Solution(object):
    def _createSingleWordDict(self, b):
        singleDict = {}
        for char in b:
            if char not in singleDict:
                singleDict[char] = 0
            singleDict[char] += 1
        return singleDict

    def _createUniversalDict(self, B):
        universalDict = {}
        for b in B:
            singleWordDict = self._createSingleWordDict(b)
            for char in singleWordDict:
                if char not in universalDict:
                    universalDict[char] = singleWordDict[char]
                elif universalDict[char] < singleWordDict[char]:
                    universalDict[char] = singleWordDict[char]
        return universalDict

    def _isSubset(self, a, universalDict):
        singleWordDict = self._createSingleWordDict(a)
        for char in universalDict:
            if char not in singleWordDict:
                return False
            elif universalDict[char] > singleWordDict[char]:
                return False
        return True

    def wordSubsets(self, A, B):
        universalDict = self._createUniversalDict(B)
        # print universalDict
        wordList = []
        for a in A:
            if self._isSubset(a, universalDict):
                wordList.append(a)
        return wordList

sol = Solution()
A = ["amazon","apple","facebook","google","leetcode"]
B = ["e", "o"]
assert sol.wordSubsets(A, B) == ["facebook","google","leetcode"]

A = ["amazon","apple","facebook","google","leetcode"]
B = ["e", "oo"]
assert sol.wordSubsets(A, B) == ["facebook","google"]


A = ["amazon","apple","facebook","google","leetcode"]
B = ["ec","oc","ceo"]
assert sol.wordSubsets(A, B) == ["facebook","leetcode"]