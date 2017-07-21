class Solution(object):
    def plusOne(self, digits):
        plus = 1
        new_digits = []
        for digit in reversed(digits):
            new_digit = str(digit + plus)
            if len(new_digit) > 1:
                new_digits.append(int(new_digit[1]))
                plus = 1
            else:
                new_digits.append(int(new_digit[0]))
                plus = 0
        if plus != 0:
            new_digits.append(plus)
        return list(reversed(new_digits))
sol = Solution()
digits = [1, 2, 3, 9]
assert sol.plusOne(digits) == [1, 2, 4, 0]
digits = [9, 9, 9]
assert sol.plusOne(digits) == [1, 0, 0, 0]
                        





