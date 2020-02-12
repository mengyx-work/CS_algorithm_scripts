class Solution(object):
    def minRemoveToMakeValid(self, s):
        # if len(s) == 0:
        #     return ''
        stack, to_remove = [], set()
        for i in range(0, len(s)):
            char = s[i]
            if char == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    to_remove.add(i)
            elif char == '(':
                stack.append(('(', i))

        while stack:
            _, idx = stack.pop()
            to_remove.add(idx)
        return ''.join([s[idx] for idx in range(len(s)) if idx not in to_remove])

sol = Solution()
s = "lee(t(c)o)de)"
assert sol.minRemoveToMakeValid(s) == 'lee(t(c)o)de'
s = ''
assert sol.minRemoveToMakeValid(s) == s