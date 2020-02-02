class Solution(object):
    results = set()
    def removeInvalidParentheses(self, s):
        lefts, rights = 0, 0
        self.results = set()
        for char in s:
            if char == '(':
                lefts += 1
            elif char == ')':
                if lefts > 0:
                    lefts -= 1
                else:
                    rights += 1
        self.dsf(s, 0, [], lefts, rights, 0)
        return list(self.results)

    def dsf(self, s, i, elems, lefts, rights, opens):
        if i == len(s):
            if lefts == 0 and rights == 0 and opens == 0:
                self.results.add(''.join(elems))
            return
        if lefts < 0 or rights < 0 or opens < 0:
            return

        elem = s[i]
        new_elems = elems[:]
        new_elems.append(elem)
        if elem == '(':
            self.dsf(s, i+1, new_elems, lefts, rights, opens+1)
            self.dsf(s, i+1, elems, lefts-1, rights, opens)
        elif elem == ')':
            self.dsf(s, i+1, new_elems, lefts, rights, opens-1)
            self.dsf(s, i+1, elems, lefts, rights-1, opens)
        else:
            self.dsf(s, i+1, new_elems, lefts, rights, opens)




sol = Solution()
# print(sol.removeInvalidParentheses("(a)())()"))

assert sol.removeInvalidParentheses("()())()") == ['(())()', '()()()']
assert sol.removeInvalidParentheses("(a)())()") == ["(a)()()", "(a())()"]
assert sol.removeInvalidParentheses(")(") == ['']

