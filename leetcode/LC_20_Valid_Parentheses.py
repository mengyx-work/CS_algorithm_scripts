# class Solution(object):
#     def isValid(self, s):
#         chrs = list(s)
#         if len(chrs) <= 1:
#             return False
#         left = {'[' : ']', '(' : ')', '{' : '}'}
#         stack = []
#         for char in chrs:
#             if char in left:
#                 stack.append(left[char])
#             elif char in left.values():
#                 if len(stack)== 0 or char != stack.pop():
#                     return False
#             else:
#                 continue
#
#         if len(stack) == 0:
#             return True
#         else:
#             return False

class Solution(object):
    def isValid(self, s):
        stack = []
        b = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in b and len(stack) > 0 and stack[-1] == b[char]:
                stack.pop()
            else:
                stack.append(char)
            # print(char, stack)
        if len(stack) == 0:
            return True
        return False

sol = Solution()
s = "(])"
print(sol.isValid(s))
s = '()[]{}'
assert sol.isValid(s) == True
# s = '(asdasd{}dasdf()[]das)'
# assert sol.isValid(s) == True
s = "([)]"
assert sol.isValid(s) == False
s = "){"
assert sol.isValid(s) == False

