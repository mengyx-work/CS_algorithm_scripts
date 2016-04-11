class Solution:

	## regualr binary search for target within a sorted array
	def sorted_seach(self, nums, target, offset):
		## target out of the boundary
		if nums[-1]<target or nums[0]>target:
			return -1
		## search wihtin the small range
		if len(nums)<=3:
			for i in xrange(len(nums)):
				if nums[i]==target:
					return (i+offset)

			return -1

		## binary search
		midIndex = len(nums)/2
		midValue = nums[midIndex]
		
		if target>midValue:
			return self.sorted_seach(nums[midIndex:], target, (offset+midIndex))
		elif target<midValue:
			return self.sorted_seach(nums[:midIndex], target, offset)
		else:
			return (offset+midIndex)

##################################

	## search for target within a rotated sorted array
	def rotated_sorted_search(self, nums, target, offset):
		if len(nums)<=3:
			for i in xrange(len(nums)):
				if nums[i]==target:
					return (i+offset)

			return -1

		midIndex = len(nums)/2
		
		if nums[0]<nums[midIndex]: ## the first half is sorted
			if nums[0]<=target and nums[midIndex]>target:
				return self.sorted_seach(nums[0:midIndex], target, offset)
			elif nums[midIndex]<nums[-1]:
				return self.sorted_seach(nums[midIndex:], target, (offset+midIndex))
			else:
				return self.rotated_sorted_search(nums[midIndex:], target, (offset+midIndex))
		else: ## the other half is sorted
			if nums[midIndex]<=target and nums[-1]>=target:
				return self.sorted_seach(nums[midIndex:], target, (offset+midIndex))
			else:
				return self.rotated_sorted_search(nums[:midIndex], target, offset)

				
##################################
	 		
  # @param {integer[]} nums
  # @param {integer} target
  # @return {integer}
	def search(self, nums, target):
		if len(nums)<=3:
			for i in xrange(len(nums)):
				if nums[i]==target:
					return i

			return -1
		return self.rotated_sorted_search(nums, target, 0)

solut = Solution()
#data = [4, 5, 6, 7, 0, 1, 2]
data = [7 ,1, 2, 3, 4, 5, 6]
print solut.search(data, 3)
				
				
