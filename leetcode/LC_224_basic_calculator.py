class Solution:
	# @param {string} s
	# @return {integer}
	def calculate(self, s):
		## only +, -, ( and ) are considered in this case
		## the sign matters and how to handle the bracket
		indx = 0
		Val = 0.
		preVal = 0
		res = 0
		sign = 1
		stack = []

		while indx<len(s):

			if s[indx]==' ':
				indx += 1
				continue

			if s[indx]=='(':
				stack.append(preVal)
				stack.append(sign)
				preVal = 0
				sign = 1
				Val = 0.


			elif s[indx]==')':
				preSign = stack.pop()
				preNum = stack.pop()
				#print 'end of bracket, Val: %i, preSign: %i, sign: %i, preVal: %i' % (Val, preSign, sign, preVal)		
				preVal = preNum + preSign*(preVal + sign*long(Val))
				sign = 1
				Val = 0.


			while ord(s[indx])<=57 and ord(s[indx])>=48:
				#print 'Val: %i, indx: %i, s[indx]: %s' % (Val, indx, s[indx])
				Val = Val*10 + (ord(s[indx]) - ord('0'))
				if indx<len(s)-1:
					if ord(s[indx+1])<=57 and ord(s[indx+1])>=48:
						indx += 1
					else:
						break
				else:
					break

			if s[indx]=='+':
				preVal += sign*long(Val)
				sign = 1
				Val = 0.

			if s[indx]=='-':
				preVal += sign*long(Val)
				sign = -1
				Val = 0.

			print 'Val: %i, indx: %i' % (Val, indx)
			indx += 1
					
	
		preVal += long(Val)*sign
		return preVal


solut = Solution()
data = '(2-(4-2)+6+(3-1))'
data = "2147483647"
print solut.calculate(data)
