import math
class Solution(object):
    def _process(self, num, base=7):
        digit = 0
        while True:
            if math.pow(base, digit) <= num and math.pow(base, digit+1) > num:
                break
            digit += 1
        digits = []
        for i in xrange(digit, -1, -1):
            base_unit = int(math.pow(base, i))
            single_digit = num / base_unit
            digits.append(str(single_digit))
            num -= single_digit * base_unit
        return ''.join(digits)

    def convertToBase7(self, num):
        if num == 0:
            return '0'
        elif num < 0:
            return '-' + self._process(abs(num))
        else:
            return self._process(num)

sol = Solution()
assert sol.convertToBase7(100) == '202'
assert sol.convertToBase7(-7) == '-10'
