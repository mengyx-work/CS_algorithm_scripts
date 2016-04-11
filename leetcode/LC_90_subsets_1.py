class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}

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
    '''

    #'''
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
    #'''


    '''
    def subsetsWithoutDup(self, nums):    
        nums.sort()
        resList = [[]]
        for elem in nums:
            print 'the resList: ', resList
            tmpList = resList[:]
            for tmp in tmpList:
                resList.append(tmp+[elem])

        return resList
    '''

solut = Solution()
nums = [1, 2, 3]
#nums = [4,1,0]
#nums = [1, 2, 2]
nums = [1, 5, 5, 5]
print solut.subsetsWithDup(nums)
