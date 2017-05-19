class Solution(object):
    def minSubArrayLen(self, s, nums):
        if len(nums) == 0:
            return 0
        start, end = 0, 0
        num_sum = 0
        for i in range(len(nums)):
            num_sum += nums[i]
            end = i
            if num_sum >= s:
                break

        if num_sum < s and end ==(len(nums) - 1):
            return 0

        min_len = end - start + 1

        while (1):
            while (num_sum - nums[start]  >= s):
                num_sum -= nums[start]
                start += 1
                min_len = min(min_len, end - start + 1)
            if end < len(nums)-1:
                end += 1
                num_sum += nums[end]
            else:
                break

        return min_len
'''
class Solution:
  # @param {integer} s
  # @param {integer[]} nums
  # @return {integer}
	def minSubArrayLen(self, s, nums):
		if len(nums)==0:
			return 0

		if len(nums)==1:
			if nums[0]==s:
				return 1
			else: 
				return 0

		startIndx, endIndx = 0, 0
		totSum = 0
		minLen = len(nums)+1
		for elem in nums:
			#print 'elem %i, totSum %i' % (elem, totSum)
			endIndx += 1
			totSum += elem
			if (totSum+elem)>=s:
				while(1):
					#print 'totSum %i, elem %i, endIndx %i, startIndx %i ' %(totSum, elem, endIndx, startIndx)
					minLen = min(minLen, (endIndx-startIndx))
					totSum -= nums[startIndx]
					startIndx +=1
					if totSum<s:
						break
		if minLen== (len(nums)+1):
			return 0
		else:
			return minLen

'''
solut = Solution()
data = [2, 3, 1, 2, 4, 3]
print solut.minSubArrayLen(7, data)
