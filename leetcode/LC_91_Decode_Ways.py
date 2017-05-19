class Solution(object):
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        cur_sets = {0: 0, 1: 0, 2: 0}
        if int(s[0]) == 1:
            cur_sets[1] = 1
        elif int(s[0]) == 2:
            cur_sets[2] = 1
        else:
            if int(s[0]) == 0:
                return 0
            cur_sets[0] = 1
        for char in s[1:]:
            tmp_set = cur_sets.copy()
            if int(char) == 1:
                cur_sets[0] = tmp_set[1] + tmp_set[2]
                cur_sets[1] = tmp_set[0] + tmp_set[1] + tmp_set[2]
                cur_sets[2] = 0
                #print char, cur_sets
                continue
            if int(char) == 2:
                cur_sets[0] = tmp_set[1] + tmp_set[2]
                cur_sets[1] = 0
                cur_sets[2] = tmp_set[0] + tmp_set[1] + tmp_set[2]
                #print char, cur_sets
                continue
            if int(char) == 0:
                cur_sets[0] = tmp_set[1] + tmp_set[2]
                cur_sets[1] = 0
                cur_sets[2] = 0
                if sum(cur_sets.values()) == 0:
                    return 0
                #print char, cur_sets
                continue
            #print char, cur_sets
            if int(char) <= 6 and int(char) > 0:
                cur_sets[0] = tmp_set[0] + 2 *(tmp_set[1]  + tmp_set[2])
            else:
                cur_sets[0] = tmp_set[0] + 2 * tmp_set[1] + tmp_set[2]
            cur_sets[1] = 0
            cur_sets[2] = 0
            #print char, cur_sets

        return sum(cur_sets.values())
            
sol = Solution()
s = '27'
assert sol.numDecodings(s) == 1
#'''
s = '26'
assert sol.numDecodings(s) == 2
s = '226'
assert sol.numDecodings(s) == 3
s = '230'
assert sol.numDecodings(s) == 0
s = '1221'
assert sol.numDecodings(s) == 5
s ='21100'
assert sol.numDecodings(s) == 0
s ='21100121'
assert sol.numDecodings(s) == 0
s = '12'
assert  sol.numDecodings(s) == 2
#'''
