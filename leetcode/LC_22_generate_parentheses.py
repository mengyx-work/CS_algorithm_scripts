class Solution(object):
    def generateParenthesis(self, n):
        lefts, rights, opens = n, n, 0
        results = []
        queue = [("", lefts, rights, opens)]
        while queue:
            subS, lefts, rights, opens = queue.pop()
            if lefts == 0 and rights == 0 and opens == 0:
                results.append(subS)
            else:
                if lefts > 0:
                    newS = subS + "("
                    queue.append((newS, lefts-1, rights, opens+1))
                if rights > 0 and opens > 0:
                    newS = subS + ")"
                    queue.append((newS, lefts, rights-1, opens-1))
        return results

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


