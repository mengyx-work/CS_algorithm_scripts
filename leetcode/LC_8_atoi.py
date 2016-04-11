class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        
        if(len(str)==0):
            return 0
        
        print str[0]
        sign = ""
        if str[0]=='+' or str[0]=='-':
            sign = str[0]
            str = str[1:]
        
        result = 0
        for i, digit in zip(xrange(len(str)), reversed(str)):
            if ord(digit)<=57 and ord(digit)>=48:
                result += int(digit)*10**i
            else:
                return 0

        if sign=="-":
            return -result
        else:
            return result


    def flexible_myAtoi(self, str):
        
        if(len(str)==0):
            return 0
        
        print str[0]
        sign = ""
        if str[0]=='+' or str[0]=='-':
            sign = str[0]
            str = str[1:]
        
        strNum = [int(x) for x in str if ord(x)<=57 and ord(x)>=48]
        result = 0
        for i, digit in zip(xrange(len(strNum)), reversed(strNum)):
            result += digit*10**i
        
        if sign=="-":
            return -result
        else:
            return result



solut = Solution()
print solut.myAtoi("+-+2")
