class Solution(object):
    '''
    Almost exactly the same as the solution to LC#39.
    Because each element can be only used once, so the search
    range in recurive function call is changed to candidates[i+1: ]
    instead of candidates[i:]
    '''
    def smart_combSum(self, candidates, target):
        resList = []
        #print candidates
        for i, elem in enumerate(candidates):
            if elem == target:
                resList.append([elem])

            if elem < target and i + 1 < len(candidates):
                possible_combns = self.smart_combSum(candidates[i+1:], target - elem)
                if len(possible_combns) != 0:
                    for combn in possible_combns:
                        resList.append([elem] + combn)
            else:
                break

        return resList

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        full_list = self.smart_combSum(candidates, target)
        clean_list = set([tuple(elem) for elem in full_list])
        return list(clean_list)
