class Solution(object):
    def checkRecord(self, s):
        ACount, LCount = 0, 0
        max_LCount = 0
        for chr in s:
            if chr == 'L':
                LCount += 1
                max_LCount = max(max_LCount, LCount)
                continue
            else:
                LCount = 0

            if chr == 'A':
                ACount += 1
                LCount = 0
                continue
        if ACount <= 1 and max_LCount <= 2:
            return True
        return False

sol = Solution()
s = 'PPALLP'
assert  sol.checkRecord(s) == True
s = 'PPALLL'
assert  sol.checkRecord(s) == False
s = 'LALL'
assert  sol.checkRecord(s) == True

                
