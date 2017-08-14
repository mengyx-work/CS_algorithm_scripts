class Solution(object):
    def removeInvalidParentheses(self, s):
        parenthesis_stack = []
        for i in xrange(len(s)):
            if s[i] =='(':
                parenthesis_stack.append((s[i], i))
            elif s[i] == ')':
                if len(parenthesis_stack) > 0 and parenthesis_stack[-1][0] == '(':
                    parenthesis_stack.pop()
                else:
                    parenthesis_stack.append((s[i], i))
        candidates = [s[:]]
        for pair in parenthesis_stack:
            tmp_candidates = []
            for candidate in candidates:
                for j in xrange(pair[1]+1):
                    if candidate[j] == pair[0]:
                        tmp_candidates.append(candidate[:j] + ' ' + candidate[j+1:])
                candidates = tmp_candidates[:]
        results = set([elem.replace(" ", "") for elem in candidates])
        return list(results)
            

sol = Solution()
assert sol.removeInvalidParentheses("()())()") == ['(())()', '()()()']
assert sol.removeInvalidParentheses("(a)())()") == ["(a)()()", "(a())()"]
assert sol.removeInvalidParentheses(")(") == ['']

