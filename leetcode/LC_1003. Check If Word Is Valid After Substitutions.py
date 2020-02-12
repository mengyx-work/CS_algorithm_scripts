class Solution(object):
    def isValid(self, S):
        if len(S) <= 2:
            return False
        stack = []
        for s in S:
            if s == 'c' and len(stack) >= 2:
                if stack[-1] == 'b' and stack[-2] == 'a':
                    stack = stack[:-2]
            else:
                stack.append(s)
        if len(stack) == 0:
            return True
        return False

sol = Solution()
S = 'abcabcababcc'
assert sol.isValid(S) == True
S = 'abccba'
assert sol.isValid(S) == False
