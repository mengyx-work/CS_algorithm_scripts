## Challenge:
## how to find the element in the sequence 
## that is more than half (or not exit at all)
## requires linear time O(n) and O(1) space. 
## How to use O(1) space to find the element from the array

class Solution:
	def majorityElement(self, nums):
		if len(nums)<=2:
			return []

		secLen = len(nums)/3
