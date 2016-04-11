class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
		lettDic = {'2':('a', 'b', 'c'), '3':('d','e','f'), '4':('g','h','i'), '5':('j','k','l'), '6':('m','n','o'), '7':('p','q','r','s'), '8':('t','u','v'), '9':('w','x','y','z')}

		resList = []
		for digit in digits:
			if digit in lettDic:
				if len(resList)==0:
					for lett in lettDic[digit]:
			 			resList.append(lett)
				else:
					tmpRes=[]
					for lett in lettDic[digit]:
						for res in resList:
							tmpRes.append(res+lett)
					resList = tmpRes

		return resList


solut = Solution()
s= '203'
print solut.letterCombinations(s)
