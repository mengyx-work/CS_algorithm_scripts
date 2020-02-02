class Solution(object):
    def dieSimulator(self, n, rollMax):
        T = 6
        if n == 0:
            return 0
        resArr = [[1 for _ in range(T)]]
        for j in range(1, n):
            res, tot = [], sum(resArr[j-1])
            for i in range(T):
                iTot = tot
                idxOffset = j - rollMax[i]
                if idxOffset >= 0 and i != j:
                    iTot -= resArr[idxOffset][i]
                res.append(iTot)
            resArr.append(res)
        print(resArr[-1])
        return sum(resArr[-1])

sol = Solution()
# n = 2
# rollMax = [1,1,2,2,2,3]
# assert sol.dieSimulator(n, rollMax) == 34
# n = 3
# rollMax = [1,1,1,2,2,3]
# assert sol.dieSimulator(n, rollMax) == 181
n = 4
rollMax = [2,1,1,3,3,2]
print(sol.dieSimulator(n, rollMax))




