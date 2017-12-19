class Solution(object):
    def getSum(self, a, b):
        a_str, b_str = list('{:b}'.format(a))[::-1], list('{:b}'.format(b))[::-1]
        a_ptr, b_ptr = 0, 0
        res = 0
        rev_str = []
        while a_ptr < len(a_str) or b_ptr < len(b_str):
            if a_ptr == len(a_str):
                tot = int(b_str[b_ptr]) + res
                b_ptr += 1
            elif b_ptr == len(b_str):
                tot = int(a_str[a_ptr]) + res
                a_ptr += 1
            else:
                tot = int(a_str[a_ptr]) + int(b_str[a_ptr]) + res
                a_ptr += 1
                b_ptr += 1
            if tot > 1:
                rev_str.append(str(tot % 2))
                res = 1
            else:
                rev_str.append(str(tot))
                res = 0
        if res > 0:
            rev_str.append(str(res))
        return int(''.join(rev_str[::-1]), 2)

sol = Solution()
a, b = 3, 2
assert sol.getSum(a, b) == a + b
a, b = 5, 0
assert sol.getSum(a, b) == a + b






