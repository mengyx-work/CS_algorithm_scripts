class Solution(object): 
    def isValid(self, s):
        chrs = list(s)
        if len(chrs) <= 1:
            return False
        left = {'[' : ']', '(' : ')', '{' : '}'}
        stack = []                            
        for char in chrs:
            if char in left:
                stack.append(left[char])
            elif char in left.values():
                if len(stack)== 0 or char != stack.pop():
                    return False
            else:
                continue

        if len(stack) == 0:
            return True
        else:
            return False

sol = Solution()
s = '()[]{}'
assert sol.isValid(s) == True
s = '(asdasd{}dasdf()[]das)'
assert sol.isValid(s) == True
s = "([)]"
assert sol.isValid(s) == False
s = "){"
assert sol.isValid(s) == False

