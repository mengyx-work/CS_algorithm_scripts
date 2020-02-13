class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        costs = []
        for i in range(len(s)):
            cost = abs(ord(s[i]) - ord(t[i]))
            costs.append(cost)
        i, j = 0, 0
        res, cur = 0, 0
        while j < len(costs):
            cur += costs[j]
            while cur > maxCost:
                cur -= costs[i]
                i += 1
            res = max(res, j - i + 1)
            j += 1

        return res


