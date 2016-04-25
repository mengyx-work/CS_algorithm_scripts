class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
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


'''
different bitwise operation to create the full list
'''
tot_num_elem = 5
total = 1 << tot_num_elem # this is the all the possible combiations, represented by bits 1111 for 4 elements

for i in range(total):
    tmp = []
    t = i
    j = 0
    for j in range(tot_num_elem): # loop through all the bits/elements to assign elements into the bit location
        if (t==0):
            break

        if (t & 1):
            tmp.append(j)

        t = t >> 1
    print i, tmp




solut = Solution()
nums = [1, 2, 3]
nums = [4,1,0]
nums = [1, 2, 2]
print solut.subsets(nums)
