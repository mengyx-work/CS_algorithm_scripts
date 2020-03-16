class Solution(object):
    def firstUniqChar(self, s):
        if len(s) == 0:
            return -1
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
        return -1

sol = Solution()
print sol.firstUniqChar('leetcode')
print sol.firstUniqChar('cc')

