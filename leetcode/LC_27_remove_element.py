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
