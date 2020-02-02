class Solution(object):
    dpResult = {}

    def dp(self, i, m):
        if (i, m) in self.dpResult:
            return self.dpResult[(i, m)]
        if 2*m >= (len(self.rightSum) - i):
            self.dpResult[(i, m)] = self.rightSum[i]
            return self.rightSum[i]
        minValue = float('inf')
        for x in range(1, 2*m+1):
            minValue = min(minValue, self.dp(i+x, max(x, m)))
        maxValue = self.rightSum[i] - minValue
        self.dpResult[(i, m)] = maxValue
        return maxValue

    def stoneGameII(self, piles):
        self.dpResult = {}
        self.rightSum = [0 for _ in range(len(piles)+1)]
        for i in range(len(piles)-1, -1, -1):
            self.rightSum[i] += self.rightSum[i+1] + piles[i]
        return self.dp(0, 1)

sol = Solution()
piles = [2,7,9,4,4]
print(sol.stoneGameII(piles))