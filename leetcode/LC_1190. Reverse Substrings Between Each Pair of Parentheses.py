class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        for chr in s:
            if chr == ')':
                string = []
                while True:
                    e = stack.pop()
                    if e == '(':
                        break
                    else:
                        string.append(e)
                stack.extend(string)
            else:
                stack.append(chr)
        return ''.join(stack)

sol = Solution()
s = "(abcd)"
assert sol.reverseParentheses(s) == "dcba"

s = "a(bcdefghijkl(mno)p)q"
assert sol.reverseParentheses(s) == "apmnolkjihgfedcbq"
