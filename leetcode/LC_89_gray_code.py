class Solution:
    def grayCodeStr(self, n):
		if n==1:
			return ['0', '1']
		tmpRes = self.grayCodeStr(n-1)
		return ['0'+elem for elem in tmpRes] + ['1'+elem for elem in reversed(tmpRes)]

    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
		if n==0:
			return [0]
		resStr = self.grayCodeStr(n)
		resNum = []
		#print resStr
		for res in resStr:
			resNum.append(int(res, 2))
		return resNum

solut = Solution()
print solut.grayCode(3)
