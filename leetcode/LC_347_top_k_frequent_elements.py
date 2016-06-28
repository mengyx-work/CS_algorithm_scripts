class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        elemDict = {}
        for elem in nums:
            if elem not in elemDict:
                elemDict[elem] = 1
            else:
                elemDict[elem] += 1

        dictPairs = elemDict.items()
        dictPairs = sorted(dictPairs, key = lambda x: x[1], reverse = True) 
            
        ## use the Counter to create the dictionary
        counter = sorted(Counter(nums).items(), key = lambda pair : pair[1])

        return [elem[0] for elem in dictPairs][0:k]

sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
nums = [4,1,-1,2,-1,2,3]
print sol.topKFrequent(nums, k)
        
        
