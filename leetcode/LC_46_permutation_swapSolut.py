class Solution:
    def creatPermut(self, nums, curIndx, maxIndx, res):
        #print 'the first nums: ', nums, 'curIndx: ', curIndx
        if curIndx==maxIndx:
            res.append(tuple(nums))
            #res.append(nums)            
            print 'the result: ', res
            return

        for i in range(curIndx, maxIndx):
            tmp1 = nums[curIndx]
            nums[curIndx] = nums[i]
            nums[i] = tmp1
            #print 'nums: ', nums 
            self.creatPermut(nums, (curIndx+1), maxIndx, res)
            
            tmp1 = nums[curIndx]
            nums[curIndx] = nums[i]
            nums[i] = tmp1



    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        resList = []
        self.creatPermut(nums, 0, len(nums), resList)
        #print 'the result to send: ', resList
        tmpRes = [list(elem) for elem in resList]
        return tmpRes


solut = Solution()
#nums = []
#nums = [1, 2]
#nums = [4,1,0, 3]
nums = [1, 1, 1, 3]
#nums = [1, 1, 2, 2, 3]
#nums = [3,3,0,0,2,3,2]
nums = [1, 1, 2, 2, 3]
nums = [1, 2, 3]
res = solut.permuteUnique(nums)
print 'the reults: ', res
