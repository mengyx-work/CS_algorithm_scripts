class Solution(object):
    def subarrayBitwiseORs(self, A):
        cur, res = set(), set()
        for a in A:
            cur = {i | a for i in cur} | {a}
            res |= cur
        return len(res)

sol = Solution()
# A = [1,1,2]
A = [1,2,4]
print(sol.subarrayBitwiseORs(A))
