class Solution(object):
    def _find_index(self, content, target):
        lb, ub = 0, len(content) - 1
        while (lb + 1 < ub):
            print lb, ub
            mid = lb + (ub - lb) / 2
            if content[mid] > target:
                ub = mid
            else:
                lb = mid
        if content[lb] == target:
            return content[lb]
        if content[ub] >= target:
            return content[ub]
        return -1

    def _match_subsequence(self, subseq, target):
        target_dict = {}
        for i, chr in enumerate(target):
            if chr not in target_dict:
                target_dict[chr] = [i]
            else:
                target_dict[chr].append(i)
        cur_idx = -1
        for chr in subseq:
            if chr not in target_dict:
                return False
            next_idx = self._find_index(target_dict[chr], cur_idx+1)
            if next_idx < 0:
                return False
            cur_idx = next_idx
        return True


    def findLUSlength(self, a, b):
        if len(a) != len(b):
            maxStr = a if len(a) >= len(b) else b
            return len(maxStr)
        else:
            if a == b:
                return -1
            else:
                return len(a)

        

sol = Solution()
#print sol._find_index([1, 2, 5, 7, 9], 6)
#print sol._match_subsequence('abbc', 'aabc')
print sol.findLUSlength('aba', 'cdc')
