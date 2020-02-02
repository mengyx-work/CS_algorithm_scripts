class Solution(object):
    def _isValidSerialization(self, preorder):
        stack = []
        for e in preorder:
            stack.append(e)
            while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
                stack = stack[:-3]
                stack.append('#')
        if len(stack) == 1 and stack[0] == '#':
            return True
        return False

    def isValidSerialization(self, preorder):
        preorder = preorder.split(',')
        return self._isValidSerialization(preorder)

sol = Solution()
preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
assert sol.isValidSerialization(preorder) == True
preorder = "9,#,#,1"
# print(sol.isValidSerialization(preorder))
assert sol.isValidSerialization(preorder) == False

preorder = "#"
assert sol.isValidSerialization(preorder) == True
preorder = "91,13,14,#,#,10"
assert sol.isValidSerialization(preorder) == False
