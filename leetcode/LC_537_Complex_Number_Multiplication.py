class Solution(object):
    def _split_num(self, a):
        aStr = a.split('+')
        return int(aStr[0]), int(aStr[1][:-1])
    def complexNumberMultiply(self, a, b):
        a_x, a_i = self._split_num(a)
        b_x, b_i = self._split_num(b)
        x = a_x * b_x  - a_i * b_i
        i = a_x * b_i + b_x * a_i
        return '{}+{}i'.format(x, i)

sol = Solution()
a = "1+1i"
b = "1+1i"
assert sol.complexNumberMultiply(a, b) == "0+2i"
a = "1+-1i"
b = "1+-1i"
assert sol.complexNumberMultiply(a, b) == '0+-2i'
