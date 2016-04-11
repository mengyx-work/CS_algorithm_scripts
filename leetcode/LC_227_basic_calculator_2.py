class Solution:
    # @param {string} s
    # @return {integer}
     def calculate(self, s):
				chrList = list(s)
				operators = set(['+', '-', '*', '/'])
				indx = 0
				preVal = 0
				res = 0
				curOptr = '+'
				curVal = 0
				
				while(indx<len(s)):
						
						if s[indx]==' ':
							indx += 1
							continue

						curVal = 0

						if s[indx]=='(':
								endIndx = indx
								leftBracketCount = 1
								while leftBracketCount>0:
										endIndx += 1
										if s[endIndx]=='(':
												leftBracketCount += 1
										elif s[endIndx]==')':
												leftBracketCount -= 1

								curVal = self.calculate(s[indx+1:endIndx])
								print 'inside bracket curVal %i' % (curVal)
								indx = endIndx

						else:
								while (ord(s[indx])<=57 and ord(s[indx])>=48):
										curVal = curVal*10 + (ord(s[indx]) - ord('0'))		
										if (indx+1)<len(s):
												indx += 1
										else:
												break

						#print 'preVal %i, curVal %i, curOptr %s' % (preVal, curVal, curOptr)

						if curOptr =='+':
								res += preVal
								preVal = curVal
						elif curOptr== '-':
								res += preVal
								preVal = -curVal
						elif curOptr =='*':
								preVal = preVal*curVal
						elif curOptr == '/':
								if preVal<0:
										preVal = -((-preVal)/curVal)
								else:
										preVal = preVal/curVal

						while (s[indx] not in operators):
								if indx+1 < len(s)-1:
										indx += 1
								else:
										break

						curOptr = s[indx]	
						indx += 1

				res += preVal
				return res

solut = Solution()
data = '(2*(1+3) - 5)'
#data = '42'
data = '4 - 2 * ( 5 +   1 )'
data = '(1+(4+5+2)-3)+(6+8)'
print solut.calculate(data)


