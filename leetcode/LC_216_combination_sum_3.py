class Solution(object):

    def smart_combinationSum3(self, k, n, thres):
        if k == 1:
            if thres <= n and n <= 9:
                return [[n]]
            else:
                return []
        # requires recursive search
        else:
            final_result = []
            if k * thres >= n:
                return final_result
            '''
            1. incrementally loop through all the possible threshold values
            2. recursively call the smart_combinationSum3 function with different thres value
            3. only add the non-empty result from further search
            '''
            for i in range(thres, int(n/thres) + thres + 1):
                possible_combns = self.smart_combinationSum3(k - 1, n - i, i+1)
                if len(possible_combns) != 0:
                    for combn in possible_combns:
                        tmpList = [i]
                        tmpList.extend(combn)
                        final_result.append(tmpList)
            return final_result


    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.smart_combinationSum3(k, n, thres = 1)



solut = Solution()
solut.combinationSum3(k = 3, n = 9)
