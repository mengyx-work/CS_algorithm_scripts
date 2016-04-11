class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        #digit = 1
        negative = False
        digit_list = []
        
        if x<0:
            negative = True
            x = -x
            
        while x>0:
            digit_num = x%10
            digit_list.append(digit_num)
            x = x/10
            #digit += 1
            
        output = 0
        print len(digit_list)

        for digit, digit_num in zip(range(len(digit_list)), list(reversed(digit_list))):
            output += digit_num*(digit**10)
            print output
        if negative:
            output = -output
            
        return output



solut = Solution()

print solut.reverse(1)
