class Solution(object):
    def removeOuterParentheses(self, S):
        ans, count, state = [], 0, False
        for s in S:
            if s == '(':
                count -= 1
            else:
                count += 1

            if count == 0:
                state = False

            if count == -1 and state is False:
                state = True
                continue

            if state is True and count < 0:
                ans.append(s)
        return ''.join(ans)

sol =Solution()
S = '(()())(())'
assert sol.removeOuterParentheses(S) == '()()()'
S = '(()())(())(()(()))'
assert sol.removeOuterParentheses(S) == '()()()()(())'


