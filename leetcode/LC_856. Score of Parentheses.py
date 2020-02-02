class Solution(object):
    def scoreOfParentheses(self, S):
        stack = []
        for s in S:
            if s == ')':
                elem = stack.pop()
                if elem == '(':
                    stack.append(1)
                else:
                    curSum = elem
                    while stack[-1] != '(':
                        elem = stack.pop()
                        curSum += elem
                    _ = stack.pop()
                    stack.append(2*curSum)
            else:
                stack.append(s)
        return sum(stack)

sol = Solution()
S = "(()(()))"
assert sol.scoreOfParentheses(S) == 6
S = "()"
assert sol.scoreOfParentheses(S) == 1
S = ""
assert sol.scoreOfParentheses(S) == 0

