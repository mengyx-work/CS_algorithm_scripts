class Solution(object):
    def _process_wildcard(self, s, p):
        '''pattern is `de*|abc*` after
        the first *;
        s is the regular string starting 
        with the same index: de|ccabcd
        '''
        if len(p) == 0 or p == '*':
            return True
        if len(s) == 0:
            return False
        pattern = []
        for char in p:
            if char == '*' or char == '?':
                if len(pattern) != 0:
                    break
                else:
                    p = p[1:]
            else:
                pattern.append(char)
        pattern_len = len(pattern)
        if pattern_len == 0:
            return True
        if pattern_len >= len(s)-1:
            return False
        candidate_results, candidate_index = [], []
        #print 'pattern: ', ''.join(pattern)
        #print 'string: ', s
        for i, char in enumerate(s[:(len(s)-pattern_len+1)]):
            #print i, char, s[i:(i+pattern_len)]
            if s[i:(i+pattern_len)] == ''.join(pattern):
                candidate_index.append(i)
        if len(candidate_index) == 0:
            return False
        for index in candidate_index:
            if pattern_len < len(p):
                #print 'partial string: ', s[(index+pattern_len):]
                candidate_results.append(self.isMatch(s[(index+pattern_len):], p[pattern_len:]))
            else:
                candidate_results.append(True)
        #print candidate_index, candidate_results
        return any(candidate_results)

    def isMatch(self, s, p):
        #print 'isMatch: ', s, p
        if len(s) == 0:
            if len(p) == 0 or p == '*':
                return True
            else:
                return False
        for i, char in enumerate(s):
            if i >= len(p):
                return False
            if p[i] == char or p[i] == '?':
                continue
            elif p[i] == '*':
                return self._process_wildcard(s[i:], p[(i+1):])
            else:
                return False
        for char in p[len(s):]:
            if char != '*':
                return False
        return True

sol = Solution()
string = 'a'
pattern = 'a*'
assert sol.isMatch(string, pattern) == True

#'''
string = 'ab'
pattern = '?*'
assert sol.isMatch(string, pattern) == True
pattern = 'a'
assert sol.isMatch(string, pattern) == False
string = 'edede'
pattern = 'de*'
assert sol._process_wildcard(string, pattern) == True
pattern = 'de'
assert sol._process_wildcard(string, pattern) == True
pattern = '*ee'
assert sol._process_wildcard(string, pattern) == False
pattern = 'de*f'
assert sol._process_wildcard(string, pattern) == False
#'''
