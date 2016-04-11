class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        digits = list(str(n))
        totNum = 0
        if len(digits)==1:
            return 1

        for i in range(len(digits)):
            if i==0:
                rightLen = len(digits[1:])
                rightDigits = int(''.join(digits[1:]))
                leftDigits = 0
            elif i==(len(digits)-1):
                leftDigits = int(''.join(digits[:-1]))
                rightDigits = 0
                rightLen = 0
            else:
                leftDigits = int(''.join(digits[:i]))
                rightDigits = int(''.join(digits[i+1:]))                
                rightLen = len(digits[i+1:])

            if int(digits[i])==0:
                totNum += leftDigits*(10**rightLen)
            elif int(digits[i])==1:
                totNum += leftDigits*(10**rightLen)+rightDigits+1
            else:
                totNum += (leftDigits+1)*(10**rightLen)
            
        return totNum


solut = Solution()
print solut.countDigitOne(10)
