class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            if nums[0]>nums[1]:
                return nums[0]
            else:
                return nums[1]
        if len(nums)==3:
            return max(nums)

        fwdRes0 = nums[0]
        fwdRes1 = max(nums[0], nums[1])
        
        fwdRes2 = nums[1]
        fwdRes3 = max(nums[1], nums[2])

        bwdRes0 = nums[0]
        bwdRes1 = max(nums[0], nums[-1])
        
        for elem in nums[2:-1]:
            tmp = max(fwdRes1, fwdRes0+elem)
            fwdRes0 = fwdRes1
            fwdRes1 = tmp

        for elem in nums[3:]:
            tmp = max(fwdRes3, fwdRes2+elem)
            fwdRes2 = fwdRes3
            fwdRes3 = tmp

        '''
        for elem in reversed(nums[:-2]):
            tmp = max(bwdRes1, bwdRes0+elem)
            bwdRes0 = bwdRes1
            bwdRes1 = tmp
        '''
        return max(fwdRes1, fwdRes3)



solut = Solution()
data = [1, 2, 2 ,3, 2]
print solut.rob(data)
