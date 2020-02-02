class Solution(object):
    def validateStackSequences(self, pushed, popped):
        popIdx, pushIdx, stack = 0, 0, []
        while popIdx < len(popped) and pushIdx < len(pushed):
            elem = pushed[pushIdx]
            pushIdx += 1
            if elem != popped[popIdx]:
                stack.append(elem)
            else:
                popIdx += 1
            while stack and popIdx < len(popped) and stack[-1] == popped[popIdx]:
                stack.pop()
                popIdx += 1

        if len(stack) == 0 and popIdx == len(popped) and pushIdx == len(pushed):
            return True
        return False

sol = Solution()
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(sol.validateStackSequences(pushed, popped))

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(sol.validateStackSequences(pushed, popped))

