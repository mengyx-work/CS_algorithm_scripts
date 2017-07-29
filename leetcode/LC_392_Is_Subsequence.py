class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        cur_index = 0
        tot_count = len(list(s))
        for char in list(t):
            if char == s[cur_index]:
                cur_index += 1
                if cur_index == tot_count:
                    return True
        return False

    '''
    def _find_upper_index(self, indexs, cur_index):
        lb, ub = 0, len(indexs) - 1
        while(lb + 1 < ub):
            mid = lb + (ub - lb) / 2
            if indexs[mid] > cur_index:
                ub = mid
            else:
                lb = mid
        if indexs[lb] > cur_index:
            return indexs[lb]
        if indexs[ub] > cur_index:
            return indexs[ub]
        return -1

    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        word_dict = {}
        for i, chr in enumerate(t):
            if chr not in word_dict:
                word_dict[chr] = [i]
            else:
                word_dict[chr].append(i)
        cur_index = -1
        for chr in s:
            if chr not in word_dict:
                return False
            index_list = word_dict[chr]
            found_index = self._find_upper_index(index_list, cur_index)
            if found_index == -1:
                return False
            cur_index = found_index
        return True
        '''

sol = Solution()
s = "abc"
t = "ahbgdc"
assert sol.isSubsequence(s, t) == True

s = "axc"
t = "ahbgdc"
assert sol.isSubsequence(s, t) == False

