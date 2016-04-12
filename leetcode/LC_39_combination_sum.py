class Solution(object):
    '''
    Similar to the other combination sum problems, a recurive call
    to the smart_combSum function is used to collect all the possible
    combinations.

    the list is sorted in the first place.
    '''
    def smart_combSum(self, candidates, target):
        resList = []
        #print candidates
        for i, elem in enumerate(candidates):
            if elem == target:
                resList.append([elem])

            if elem < target and i < len(candidates):
                possible_combns = self.smart_combSum(candidates[i:], target - elem)
                if len(possible_combns) != 0:
                    for combn in possible_combns:
                        resList.append([elem] + combn)
            else:
                break

        return resList

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.smart_combSum(candidates, target)
