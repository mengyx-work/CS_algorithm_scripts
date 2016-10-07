class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLst = []
        sDic = {}
        for i, chr in enumerate(s):
            sLst.append(chr)
            if chr in sDic:
                sDic[chr] = -1
            else:
                sDic[chr] = i
        for key in sLst:
            if sDic[key] != -1:
                return sDic[key]

sol = Solution()
print sol.firstUniqChar('leetcode')

