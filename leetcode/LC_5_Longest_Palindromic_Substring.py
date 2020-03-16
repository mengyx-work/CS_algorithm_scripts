class Solution(object):
    def _find_max_len(self, s, start, end):
        while(start >= 0 and end < len(s) and s[start] == s[end]):
            start -= 1
            end += 1
        return s[start+1:end]

    def longestPalindrome(self, s):
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s

        substr = s[0]
        for i in range(len(s)-1):
            tmpStr = self._find_max_len(s, i, i)
            if len(tmpStr) > len(substr):
                substr = tmpStr
            #print max_len, i
            if s[i] == s[i+1]:
                tmpStr = self._find_max_len(s, i, i+1)
                if len(tmpStr) > len(substr):
                    substr = tmpStr
        return substr

sol = Solution()
s = 'babad'
print sol.longestPalindrome(s)

        
