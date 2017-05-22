class Solution(object):
    def _valid_string_length(self, s):
        stack = []
        valid_end = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(')')
            if char == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    return valid_end
            if len(stack) == 0:
                valid_end = i + 1
        return  valid_end

    def longestValidParentheses(self, s):
        max_len = 0
        stack = []
        prefix_start = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(')')
                prefix_length = (i-prefix_start-1) if i != prefix_start else i - prefix_start
                max_len = max(max_len, self._valid_string_length(s[i:]) + prefix_length)
            if char == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    prefix_start = i
        return max_len

sol = Solution()
#'''
s = '()'
assert sol.longestValidParentheses(s) == 2
#'''
s = ')()())'
assert sol.longestValidParentheses(s) == 4
s = 'aa(dd)(sds(D)sd'
assert sol.longestValidParentheses(s) == 8
s = 'aa(dd)(sds(D)sd'
#assert sol.longestValidParentheses(s) == 4
#'''

#'''
s = '())'
assert sol._valid_string_length(s)  == 2
s = '()aa'
assert sol._valid_string_length(s)  == 4
s = '(()('
assert sol._valid_string_length(s) == 0
s = '(())aa'
assert sol._valid_string_length(s) == 6
s = '(()())'
assert sol._valid_string_length(s) == 6
s = '(('
assert sol._valid_string_length(s) == 0
#'''
