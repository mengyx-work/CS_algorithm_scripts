class Solution(object):
    def candy(self, ratings):
        '''simple and elegant `hill` solution
        '''
        if len(ratings) == 0:
            return 0
        candies = [1]
        for prev_i, rating in enumerate(ratings[1:]):
            if rating > ratings[prev_i]:
                candies.append(candies[-1] + 1)
            else:
                candies.append(1)
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
                candies[i-1] = candies[i] + 1
        return sum(candies)

    '''
    def _check_candies(self, candies, ratings, cur_i):
        #print 'before check candies: ', candies
        for i in range(cur_i, 0, -1):
            if ratings[i] < ratings[i-1] and candies[i] >= candies[i-1]:
                candies[i-1] = candies[i] + 1
            else:
                break

    def candy(self, ratings):
        if len(ratings) == 0:
            return 0
        candies = [1]
        for prev_i, rating in enumerate(ratings[1:]):
            if rating > ratings[prev_i]:
                candies.append(candies[-1]+1)
            elif rating == ratings[prev_i]:
                candies.append(1)
                continue
            else:
                candies.append(1)
                if ratings[prev_i] > ratings[prev_i+1]:
                    self._check_candies(candies, ratings, prev_i+1)
        return sum(candies)
    '''

sol = Solution()
nums = [1, 2, 3, 4, 5]
assert sol.candy(nums) == sum(nums)
nums = [4, 1, 3, 2, 7, 5]
assert sol.candy(nums) == 9
nums = [1,2,2]
assert sol.candy(nums) == 4




