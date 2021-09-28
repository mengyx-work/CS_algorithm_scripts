class Solution(object):
    ## two pointers
    def removeElement(self, nums, val):
        l, r = 0, len(nums) - 1
        while l < r:
            while nums[l] != val and l < (len(nums) - 1):
                l += 1
            while nums[r] == val and 0 < r:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        while l < len(nums) and nums[l] != val:
            l += 1
        return l

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        new_list = []
        print 'length:', len(nums)
        for i in range(0, 2):
            print 'nums value: ', nums[i]
            print 'i: ', i
            if nums[i]!=val:
                #print 'nums value:', nums[i]
                #print 'i: ', i
                new_list.append(nums[i])
            
            #print new_list
            nums = new_list
            return len(nums)




data = [3, 3]
solution = Solution()
result = solution.removeElement(data, 5)
print result
print data
