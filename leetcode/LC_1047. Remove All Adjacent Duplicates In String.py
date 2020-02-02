class Solution(object):
    def removeDuplicates(self, S):
        stack = []
        for s in S:
            if stack and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        return ''.join(stack)

sol = Solution()
S = "abbaca"
print(sol.removeDuplicates(S))
