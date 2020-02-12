class Solution(object):
    def combine(self, n, k):
        results = []
        if n < k:
            return results
        self.dfs(results, [], 1, n, k)
        return results

    def dfs(self, results, curRes, idx, n, k):
        if k == 0:
            results.append(curRes)
        if idx > n:
            return
        tmpRes = curRes[:]
        for i in range(idx, n+1):
            tmpRes.append(i)
            self.dfs(results, tmpRes, i+1, n, k-1)
            tmpRes = tmpRes[:-1]

solut = Solution()
print solut.combine(4, 2)

# class Solution:
# 	def creatComb(self, nums, k):
# 		resList = []
# 		if k==1:
# 			for num in nums:
# 				resList.append([num])
# 		else:
# 			for i in range(len(nums)-k+1):
# 				num = nums[i]
# 				tmpNums = nums[i+1:]
# 				for res in self.creatComb(tmpNums, k-1):
# 					resList.append([num]+res)
# 		return resList
#
#     # @param {integer} n
#     # @param {integer} k
#     # @return {integer[][]}
# 	def combine(self, n, k):
# 		nums = [i for i in range(1, n+1)]
# 		resList = self.creatComb(nums, k)
# 		return resList
#
#
# '''
# different solution
# '''
#
# class Solution(object):
#
#     def smart_combine(self, k, n, thres):
#
#         final_result = [] # default to be empty
#
#         if k == 1:
#             if thres <= n:
#                 for i in range(thres, n+1):
#                     final_result.append([i])
#
#             return final_result
#
#         # requires recursive search
#         else:
#             for i in range(thres, n + 1):
#                 possible_combns = self.smart_combine(k - 1, n, i+1)
#                 if len(possible_combns) != 0:
#                     for combn in possible_combns:
#                         tmpList = [i]
#                         tmpList.extend(combn)
#                         final_result.append(tmpList)
#
#             return final_result
#
#
#     def combine(self, n, k):
#         """
#         :type k: int
#         :type n: int
#         :rtype: List[List[int]]
#         """
#         return self.smart_combine(k, n, thres = 1)

