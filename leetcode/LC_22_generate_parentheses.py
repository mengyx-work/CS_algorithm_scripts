class Solution(object):
    def _count_left_parenthesis(self, s):
        total_count, extra_count = 0, 0
        chars = list(s)
        for char in chars:
            if char == '(':
                total_count += 1
                extra_count += 1
            if char ==')':
                extra_count -= 1
        return total_count, extra_count

    def generateParenthesis(self, n):
        candidates = ['(']
        for i in range(2*n-1):
            tmp_candidates = []
            for candidate in candidates:
                total_count, extra_count = self._count_left_parenthesis(candidate)
                if extra_count > 0:
                    if total_count < n:
                        tmp_candidate = candidate + '('
                        tmp_candidates.append(tmp_candidate)
                    tmp_candidate = candidate + ')'
                    tmp_candidates.append(tmp_candidate)
                else: 
                    tmp_candidate = candidate + '('
                    tmp_candidates.append(tmp_candidate)
            candidates = tmp_candidates
        return candidates
sol = Solution()
print sol.generateParenthesis(3)
               
'''
def addParenthsis(left, right, single_str, str_list):
    #print single_str
    if left==0 and right==0:
        str_list.append(single_str)
        return
    if left < right:
        if(left>0):
            addParenthsis(left-1, right, single_str+"(", str_list)
        if(right>0):
            addParenthsis(left, right-1, single_str+")", str_list)
    else:
        if(left>0):        
            addParenthsis(left-1, right, single_str+"(", str_list)

def generateParenthesis(n):
    str_list = []
    str=''
    addParenthsis(n, n, str, str_list)
    return str_list
string_list = generateParenthesis(4)
print string_list
'''


