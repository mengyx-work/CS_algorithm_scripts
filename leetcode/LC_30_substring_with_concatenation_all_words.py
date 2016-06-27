class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ## words may contain duplicated words, use dictionary instead of set
        ## and convert dicionary into set of tuples to compare
        def convert_list2dict(input_list):
            dictionary = {}
            for elm in input_list:
                if elm not in dictionary:
                    dictionary[elm] = 1
                else:
                    dictionary[elm] += 1
            return dictionary
        
        wordDict = convert_list2dict(words)
        
        if len(words) == 0 or len(s) == 0:
            return []

        wordLen = len(words[0])
        totLen = len(words) * wordLen
        wordIndex = range(0, totLen, wordLen)
        #print wordIndex

        if len(s) < totLen:
            return []

        index_array = []

        for index in range(len(s) - totLen + 1):
            substring = s[index:(index + totLen)]
            test_substring = [substring[i:(i+wordLen)] for i in wordIndex]
            testDict = convert_list2dict(test_substring)
            if set(wordDict.items()) == set(testDict.items()):
                index_array.append(index)

        return index_array



sol = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
#s = "wordgoodgoodgoodbestword"
#words = ["word","good","best","good"]
res = sol.findSubstring(s, words)
print res
