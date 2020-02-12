class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        counts = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        n = min(10, n)
        prod, result = 1, 1
        for i in range(n):
            prod *= counts[i]
            result += prod
        return result

# class Solution(object):
#     def countNumbersWithUniqueDigits(self, n):
#         counts = {0 : 1, 1 : 10}
#         for i in xrange(2, 11):
#             max_cur_digit = 9
#             tot = 9
#             for j in xrange(i-1):
#                 tot *= max_cur_digit
#                 max_cur_digit -= 1
#             counts[i] = tot + counts[i-1]
#         return counts.get(n, counts[10])

sol = Solution()
print sol.countNumbersWithUniqueDigits(2)



