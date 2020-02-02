class Solution(object):
    def removeDuplicateLetters(self, s):
        res = {}
        for i in len(s):
            if s[i] not in res:
                res[s[i]] = i
            else:
                res[s[i]]

