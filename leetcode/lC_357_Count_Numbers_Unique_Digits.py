class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        counts = {0 : 1, 1 : 10}
        for i in xrange(2, 11):
            max_cur_digit = 9
            tot = 9
            for j in xrange(i-1):
                tot *= max_cur_digit
                max_cur_digit -= 1
            counts[i] = tot + counts[i-1]
        return counts.get(n, counts[10])
sol = Solution()
print sol.countNumbersWithUniqueDigits(2)



