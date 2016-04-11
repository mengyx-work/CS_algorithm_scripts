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
