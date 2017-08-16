class Solution:
    def _add_element(self, nums, start_idx, cur_result, results):
        results.append(cur_result)
        if start_idx >= len(nums):
            return
        prev_idx = None
        for i in xrange(start_idx, len(nums)):
            tmp_result = cur_result[:]
            tmp_result.append(nums[i])
            if prev_idx is not None and nums[i] == nums[prev_idx]:
                continue
            else:
                self._add_element(nums, i+1, tmp_result, results)
                prev_idx = i

    def subsetsWithDup(self, nums):
        if len(nums) == 0:
            return []
        nums.sort()
        results = []
        self._add_element(nums, 0, [], results)
        return results

sol = Solution()
nums = [1, 2, 3]
#nums = [4,1,0]
#nums = [1, 2, 2]
#nums = [1, 5, 5, 5]
nums = [4,4,4,1,4]
assert sol.subsetsWithDup(nums) == [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

'''
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            print 'l:', l, 'i: ', i
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res

    def subsetsWithDup(self, nums):
        nums.sort()
        resList = []
        self.dfs(nums, 0, [], resList)
        return resList

    def dfs(self, nums, pos, tmpList, resList):
        #print 'coming tmpList: ', tmpList, 'resList: ', resList, ' pos:', pos
        resList.append(tmpList[:])
        #print 'resList: ', resList
        #print 'pos: {}'.format(pos)
        for i in range(pos, len(nums)):
            #print 'i: ', i, ' tmpList: ', tmpList
            #print 'i: {0}, pos: {1}'.format(i, pos)
            if i==pos or nums[i]!=nums[i-1]:
                tmpList.append(nums[i])
            #print 'tmpList: ', tmpList, 'resList: ', resList
                self.dfs(nums, i+1, tmpList, resList)
                tmpList.pop()
'''



