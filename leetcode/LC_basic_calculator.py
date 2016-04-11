class Solution:
	def calc(self, a, b, sign):
		if sign=="-":
			return (int(a)-int(b))
		if sign=="+":
			return (int(a)+int(b))
		if sign=="*":
			return (int(a)*int(b))
		if sign=="/":
			return (int(a)/int(b))


	def calculator(self, s):
		operators = set(['+', '-', '*', '/'])
		chrList = list(s)
		leftValue = 0
		i=0
		while(i<len(chrList)):
			if chrList[i] in operators:
				leftValue = self.calc(leftValue, chrList[i], chrList[i+1])
				i += 2
			else:
				leftValue = chrList[i]
				i += 1
			print 'leftValue: ', leftValue


		return  leftValue


solut = Solution()
data = "1+2+4"
print solut.calculator(data)



