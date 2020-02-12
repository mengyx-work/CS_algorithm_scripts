import math


class Solution(object):
    '''
    the DFS approach
    '''
    def getFactors(self, n):
        results = []
        self.dsf(n, results, [], 2)
        return results

    def dsf(self, n, results, curRes, val):
        print(curRes, n, val)
        if n <= 1:
            if len(curRes) > 1:
                results.append(curRes)
            return
        tmpRes = curRes[:]
        for i in range(val, int(math.sqrt(n))+1):
            if n % i == 0:
                tmpRes.append(i)
                self.dsf(n / i, results, tmpRes, i)
                tmpRes = tmpRes[:-1]
        tmpRes.append(n)
        self.dsf(1, results, tmpRes, n)

# class Solution(object):
#     def getFactors(self, n):
#         results = self._getFactors(n, 2, init=True)
#         return results
#
#     def _getFactors(self, n, minV, init=False):
#         '''
#         BFS approach
#         :param n:
#         :param minV:
#         :param init:
#         :return:
#         '''
#         if init:
#             results = []
#         else:
#             results = [[n]]
#         for i in range(minV, int(math.sqrt(n))+1):
#             subF = n % i
#             if subF == 0:
#                 resultArr = self._getFactors(n / i, i)
#                 for result in resultArr:
#                     results.append([i] + result)
#         return results

sol = Solution()
print(sol.getFactors(12))
# print(sol.getFactors(32))