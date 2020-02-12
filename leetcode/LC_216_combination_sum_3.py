class Solution(object):
    def combinationSum3(self, k, n):
        results = []
        if k > n:
            return results
        self.dfs(results, [], 1, n, k)
        return results

    def dfs(self, results, curRes, idx, n, k):
        if k == 0 and n == 0:
            results.append(curRes)
        if k <= 0:
            return
        tmpRes = curRes[:]
        for i in range(idx, 10):
            tmpRes.append(i)
            self.dfs(results, tmpRes, i+1, n-i, k-1)
            tmpRes = tmpRes[:-1]

sol = Solution()
print(sol.combinationSum3(3, 7))

# class Solution(object):
#
#     def smart_combinationSum3(self, k, n, thres):
#         if k == 1:
#             if thres <= n and n <= 9:
#                 return [[n]]
#             else:
#                 return []
#         # requires recursive search
#         else:
#             final_result = []
#             if k * thres >= n:
#                 return final_result
#             '''
#             1. incrementally loop through all the possible threshold values
#             2. recursively call the smart_combinationSum3 function with different thres value
#             3. only add the non-empty result from further search
#             '''
#             for i in range(thres, int(n/thres) + thres + 1):
#                 possible_combns = self.smart_combinationSum3(k - 1, n - i, i+1)
#                 if len(possible_combns) != 0:
#                     for combn in possible_combns:
#                         tmpList = [i]
#                         tmpList.extend(combn)
#                         final_result.append(tmpList)
#             return final_result
#
#
#     def combinationSum3(self, k, n):
#         """
#         :type k: int
#         :type n: int
#         :rtype: List[List[int]]
#         """
#         return self.smart_combinationSum3(k, n, thres = 1)



solut = Solution()
solut.combinationSum3(k = 3, n = 9)
