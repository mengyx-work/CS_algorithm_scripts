# import math
# class Solution(object):
#     def consecutiveNumbersSum(self, N):
#         """
#         :type N: int
#         :rtype: int
#         """
#         count = 0
#         max_length = int(math.sqrt(2*N))
#         for i in range(1, max_length+1):
#             test_num = N - i*(i-1)/2
#             if test_num > 0 and test_num % i == 0:
#                 count += 1
#         return count

class Solution(object):
    def consecutiveNumbersSum(self, N):
        k, cnt = 1, 1
        while 2*N >= (k+1)*(k+2):
            if (2*N - k*(k+1)) % (2*(k+1)) == 0:
                cnt += 1
                # print(k)
            k += 1
        return cnt

sol = Solution()
assert sol.consecutiveNumbersSum(15) == 4
assert sol.consecutiveNumbersSum(9) == 3
assert sol.consecutiveNumbersSum(5) == 2
assert sol.consecutiveNumbersSum(3) == 2

