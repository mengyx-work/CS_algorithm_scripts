class Solution(object):
    def subtractProductAndSum(self, n):
        if n == 0:
            return 0
        prod, sum = 1, 0
        for s in str(n):
            prod *= int(s)
            sum += int(s)
        return prod - sum