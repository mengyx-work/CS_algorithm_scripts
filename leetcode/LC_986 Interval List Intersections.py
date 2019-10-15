class Solution(object):
    def intervalIntersection(self, A, B):
        ans = []
        cur_a, cur_b = None, None
        while (len(A) > 0 or cur_a is not None) and (len(B) > 0 or cur_b is not None):
            if cur_a is None:
                cur_a = A.pop(0)
            if cur_b is None:
                cur_b = B.pop(0)
            i = max(cur_a[0], cur_b[0])
            j = min(cur_a[1], cur_b[1])
            if i <= j:
                ans.append([i, j])
            if cur_a[1] >= cur_b[1]:
                cur_b = None
            else:
                cur_a = None
        return ans

sol = Solution()
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(sol.intervalIntersection(A, B))

