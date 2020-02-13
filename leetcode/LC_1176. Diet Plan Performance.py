class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        res, j, tot = 0, 0, 0
        while j < len(calories):
            tot += calories[j]
            if j + 1 > k:
                tot -= calories[j-k]
            if j + 1 >= k:
                if tot < lower:
                    res -= 1
                if tot > upper:
                    res += 1
            # print(j, tot, res)
            j += 1
        return res

sol = Solution()
calories = [1,2,3,4,5]
print(sol.dietPlanPerformance(calories, 1, 3, 3))
calories = [3, 2]
print(sol.dietPlanPerformance(calories, 2, 0, 1))

