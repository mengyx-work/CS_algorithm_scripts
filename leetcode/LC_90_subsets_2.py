class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
   def subsetsWithDup(self, nums):
		resList = [[]]
		for num in nums:
			tmpList = resList[:]
			for res in resList:
				print 'res: ', res
				tmpRes = res[:]
				tmpRes.append(num)
				tmpList.append(tmpRes)
			#print 'tmpList: ', tmpList
			resList[:] = tmpList[:]
			#print 'resList: ', resList

		resSet = set([])
		finalRes = []
		for elem in resList:
			if len(elem)!=0:
				#print 'the elem: ', elem				
				elem.sort()
				#print tmp
				resSet.add(tuple(elem))

		finalRes.append([])
		for elem in resSet:
			finalRes.append(list(elem))
		return finalRes


solut = Solution()
nums = [1, 2, 3]
nums = [4,1,0]
nums = [1, 2, 2, 2]
nums = [1, 1, 2, 2, 3]
print solut.subsets(nums)	 
