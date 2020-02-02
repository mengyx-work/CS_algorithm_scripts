class Solution(object):
    def calPoints(self, ops):
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                val = stack[-1]
                stack.append(2*val)
            elif op == '+':
                val = sum(stack[-2:])
                stack.append(val)
            else:
                stack.append(int(op))
        return sum(stack)

sol = Solution()
ops = ["5","2","C","D","+"]
assert sol.calPoints(ops) == 30
ops = ["5","-2","4","C","D","9","+","+"]
assert sol.calPoints(ops) == 27

