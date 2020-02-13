class Solution(object):
    def wordPattern(self, pattern, str):
        patternDic = {}
        pattern = list(pattern)
        words = str.split(' ')

        if len(pattern) != len(words):
            return False

        for i, elem in enumerate(pattern):
            if elem not in patternDic:
                if words[i] in patternDic.values():
                    return False
                else:
                    patternDic[elem] = words[i]
            else:
                if patternDic[elem] != words[i]:
                    return False
        return True

sol = Solution()
print sol.wordPattern('abba', 'dog cat cat dog')
print sol.wordPattern('abba', 'dog dog dog dog')
print sol.wordPattern('abaa', 'dog cat cat dog')
