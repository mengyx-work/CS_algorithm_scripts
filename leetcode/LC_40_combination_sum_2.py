
class Solution(object):
    def combinationSum2(self, candidates, target):
        results = []
        candidates.sort()
        print(candidates)
        self.dfs(candidates, target, results, [], 0)
        return results

    def dfs(self, candidates, target, results, curRes, idx):
        if target < 0:
            return
        if target == 0:
            results.append(curRes)
        tmpRes = curRes[:]
        print(curRes, target, idx)
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            tmpRes.append(candidates[i])
            self.dfs(candidates, target-candidates[i], results, tmpRes, i+1)
            tmpRes = tmpRes[:-1]

sol = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(sol.combinationSum2(candidates, target))

# class Solution(object):
#     '''
#     Almost exactly the same as the solution to LC#39.
#     Because each element can be only used once, so the search
#     range in recurive function call is changed to candidates[i+1: ]
#     instead of candidates[i:]
#     '''
#     def smart_combSum(self, candidates, target):
#         resList = []
#         #print candidates
#         for i, elem in enumerate(candidates):
#             if elem == target:
#                 resList.append([elem])
#
#             if elem < target and i + 1 < len(candidates):
#                 possible_combns = self.smart_combSum(candidates[i+1:], target - elem)
#                 if len(possible_combns) != 0:
#                     for combn in possible_combns:
#                         resList.append([elem] + combn)
#             else:
#                 break
#
#         return resList
#
#     def combinationSum2(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         candidates.sort()
#         full_list = self.smart_combSum(candidates, target)
#         clean_list = set([tuple(elem) for elem in full_list])
#         return list(clean_list)
