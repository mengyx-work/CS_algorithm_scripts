class Solution():
    def decode_string(self, string, left='[', right=']'):
        ''' recursive approach to unfold
        the parentheses one at a time
        '''
        left_index = None
        content = list(string)
        for i, char in enumerate(content):
            if char == left:
                left_index = i
            if char == right:
                unfold_string = content[:left_index-1] + int(content[left_index-1]) * content[left_index+1:i] + content[i+1:]
                return self.decode_string(unfold_string, left, right)
        if left_index is None:
            return ''.join(content)

    def decode_string(self, string, left='[', right=']'):
        ''' iterative approach to unfold
        one at a time and append the result
        to the previous parentheses
        '''
        string_list= list(string)
        single_cntent = []
        contents = []
        for char in string_list:
            if char == left:
                contents.append((single_cntent[:-1], int(single_cntent[-1])))
                single_cntent = []
            elif char == right:
                pre_content, multiplier = contents.pop()
                single_cntent = pre_content + multiplier * single_cntent
                print single_cntent
            else:
                single_cntent.append(char)
        return ''.join(single_cntent)

sol = Solution()
content = "aa2[bb2[cc]dd2[ee]f]gg"
result = "aa" + 2*"bbccccddeeeef" + "gg"
assert sol.decode_string(content) == result




        

