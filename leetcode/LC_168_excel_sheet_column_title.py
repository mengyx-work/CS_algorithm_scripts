class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        digit_num = 0
        digits = []
        while n>0:
            digit = n%26
            ## key point: the maximum value is 26
            if digit==0:
                digit = 26
            digits.append(digit)
            n = n - digit
            n = n/26
        print digits
        result = ''
        for digit in reversed(digits):
            result += chr(64+digit)

        return result



    '''
    def convertToTitle(self, n):
        digit_num = 0
        digits = []

        while n>0:
            print n
            digits.append((n%26))

            digit_num += 1
            n = n/26

        result = ''
        print digits
        #for i, num in zip(digit, range(len(digit)-1, 0, -1)):
        for digit in digits:
            result += chr(64+digit)

        return result
    '''

solut = Solution()
print solut.convertToTitle(26*26)
