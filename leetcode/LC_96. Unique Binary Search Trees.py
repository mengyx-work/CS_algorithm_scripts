class Solution(object):
    def numTrees(self, n):
        count = {0: 1, 1: 1}
        for i in range(2, n+1):
            tot = 0
            for j in range(i):
                tot += count[j]*count[i-j-1]
            count[i] = tot
        return count[n]

