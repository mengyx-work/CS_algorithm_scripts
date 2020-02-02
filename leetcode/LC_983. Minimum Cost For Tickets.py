class Solution(object):
    def mincostTickets(self, days, costs):
        dayCosts, totCost = [0], 0
        for i in range(1, 366):
            if i in days:
                if i > 29:
                    one = dayCosts[i - 1] + costs[0]
                    seven = dayCosts[i - 7] + costs[1]
                    thirty = dayCosts[i - 30] + costs[2]
                elif i > 6:
                    one = dayCosts[i - 1] + costs[0]
                    seven = dayCosts[i - 7] + costs[1]
                    thirty = costs[2]
                elif i > 1:
                    one = dayCosts[i - 1] + costs[0]
                    seven = costs[1]
                    thirty = costs[2]
                else:
                    one, seven, thirty = costs[0], costs[1], costs[2]
                minCost = min([one, seven, thirty])
                totCost += minCost
                dayCosts.append(minCost)
            else:
                dayCosts.append(dayCosts[-1])
        return minCost

sol = Solution()
days = [1,4,6,7,8,20]
costs = [2,7,15]
assert sol.mincostTickets(days, costs) == 11

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
print(sol.mincostTickets(days, costs))
assert sol.mincostTickets(days, costs) == 17
