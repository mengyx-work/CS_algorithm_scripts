class Solution(object):
    def minAddToMakeValid(self, S):
        stack = []
        for s in S:
            if stack and s == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
        return len(stack)

sol = Solution()
S = "()))(("
print(sol.minAddToMakeValid(S))