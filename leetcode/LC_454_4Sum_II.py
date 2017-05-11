class Solution(object):
    def create_combination_dcit(self, A, B):
        combo_dict = {}
        for a in A:
            for b in B:
                elem = a + b
                if elem in combo_dict:
                    combo_dict[elem] += 1
                else:
                    combo_dict[elem] = 1
        return combo_dict
 
    def fourSumCount(self, A, B, C, D):
        combo_dict_1, combo_dict_2 = self.create_combination_dcit(A, B), self.create_combination_dcit(C, D)
        count = 0
        for key in combo_dict_1.keys():
            if -key in combo_dict_2:
                count += combo_dict_1[key] * combo_dict_2[-key]
        return count

sol = Solution()
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print sol.fourSumCount(A, B, C, D)


