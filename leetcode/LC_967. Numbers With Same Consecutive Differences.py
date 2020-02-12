class Solution(object):
    def numsSameConsecDiff(self, N, K):
        results = []
        if N == 0:
            return []
        self.dfs(results, '', N, K, True)
        return results

    def dfs(self, results, curRes, N, K, init):
        if len(curRes) == N:
            results.append(int(curRes))
            return

        if init:
            valid_range = range(0, 10) if N == 1 else range(1, 10)
            for i in valid_range:
                self.dfs(results, str(i), N, K, False)
        else:
            tmpRes = curRes
            for i in range(0, 10):
                if abs(int(tmpRes[-1]) - i) == K:
                    self.dfs(results, tmpRes+str(i), N, K, False)

sol = Solution()
# print(sol.numsSameConsecDiff(3, 7))
assert set(sol.numsSameConsecDiff(3, 7)) == set([181,292,707,818,929])
assert set(sol.numsSameConsecDiff(2, 1)) == set([10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98])