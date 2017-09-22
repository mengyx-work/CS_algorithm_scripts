class Solution:
	def threeSum(self, nums):
		postvDict = {}
		negtvDict = {}
		zeroCount = 0
		sumList = set()
		for elem in nums:
			if elem>0:
				if elem not in postvDict:
					postvDict[elem] = 1
				else:
					postvDict[elem] += 1
			elif elem<0:
				if elem not in negtvDict:
					negtvDict[elem] = 1
				else:
					negtvDict[elem] += 1
			else:
				zeroCount += 1
		for negElem in negtvDict:
			## when zero exist
			if -negElem in postvDict and zeroCount>0:
				sumList.add((negElem, 0, -negElem))
			## loop through all the positive elements
			for posElem in postvDict:
				## check two positive elements
				if (posElem+negElem)<0 and -(posElem+negElem) in postvDict:
					if -(2*posElem)==negElem: ## requires two identical elements
						if postvDict[posElem]>=2:
							sumList.add((negElem, posElem, posElem))
					else:
						if -(posElem+negElem)>posElem:
							sumList.add((negElem, posElem, -(posElem+negElem)))
						else:
							sumList.add((negElem, -(posElem+negElem), posElem))

				## check two negative elements
				if (posElem+negElem)>0 and -(posElem+negElem) in negtvDict:
					if -(2*negElem)==posElem:
						if negtvDict[negElem]>=2: ## requires two identical elements
							sumList.add((negElem, negElem, posElem))
					else:
						if  -(posElem+negElem)<negElem:
							sumList.add((-(posElem+negElem), negElem, posElem))
						else:
							sumList.add((negElem, -(posElem+negElem), posElem))

		if zeroCount>2:
			sumList.add((0, 0, 0))

		return list(sumList)

solut = Solution()

#data = [-1,1, 2, -1, -4, -2, 1]
data = [3,0,-2,-1,1,2]
print solut.threeSum(data)
