class Solution(object):
    num_set = set([str(i) for i in range(10)])
    sign_set = set(['+', '-'])

    def _is_simple_num(self, s):
        dot_count = 0
        if s[0] not in self.num_set and s[0] not in self.sign_set:
            return False
        for char in s[1:-1]:
            if char in self.num_set or char in self.sign_set:
                continue
            if char == '.':
                if dot_count == 0:
                    dot_count = 1
                    continue
                else:
                    return False
            return False
        if s[-1] in self.num_set:
            return True
        else: 
            return False

    def isNumber(self, s):
        if len(s) == 0:
            return False
        if len(s) == 1:
            if s in self.num_set:
                return True
            else:
                return False
        dot_count = 0
        if s[0] == '.':
            dot_count = 1
        elif s[0] not in self.num_set and s[0] not in self.sign_set:
            return False
        for i, char in enumerate(s[1:-1]):
            if char in self.num_set or char in self.sign_set:
                continue
            if char == '.':
                if dot_count == 0:
                    dot_count = 1
                    continue
                else:
                    return False
            if char == 'e':
                #print char, i
                #print s[:(i+1)], s[(i+2):]
                if self._is_simple_num(s[:(i+1)]) and self._is_simple_num(s[(i+2):]):
                    continue
                else:
                    print 'here'
                    return False
            print 'last', i, char
            print char
            return False
        if s[-1] in self.num_set or (s[-1] == '.' and dot_count == 0):
            return True
        else: 
            return False

sol = Solution()
s = ". 1"
assert sol.isNumber(s) == False
s = '3.'
assert sol.isNumber(s) == True
s = '..2'
assert sol.isNumber(s) == False
s = '2e10'
assert sol.isNumber(s) == True
s = " +0.1 "
assert sol.isNumber(s) == True
s = "1 a"
assert sol.isNumber(s) == False
s = '+23e-10'
assert sol.isNumber(s) == True

            


