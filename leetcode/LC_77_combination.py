class Solution:
	def creatComb(self, nums, k):
		resList = []
		if k==1:
			for num in nums:
				resList.append([num])
		else:
			for i in range(len(nums)-k+1):
				num = nums[i]
				tmpNums = nums[i+1:]
				for res in self.creatComb(tmpNums, k-1):
					resList.append([num]+res)
		return resList
		
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
	def combine(self, n, k):
		nums = [i for i in range(1, n+1)]
		resList = self.creatComb(nums, k)
		return resList


solut = Solution()
print solut.combine(4, 2)
