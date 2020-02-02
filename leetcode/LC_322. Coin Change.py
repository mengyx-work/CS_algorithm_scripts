class Solution(object):
    def coinChange(self, coins, amount):
        coinsCounts = {0: 0}
        for coin in coins:
            coinsCounts[coin] = 1

        for i in range(1, amount+1):
            countsCandidates = []
            if i in coinsCounts:
                continue
            for coin in coins:
                money = i - coin
                if money > 0 and money in coinsCounts:
                    countsCandidates.append(coinsCounts[money] + 1)
            if len(countsCandidates) > 0:
                coinsCounts[i] = min(countsCandidates)

        # print(coinsCounts)
        if amount in coinsCounts:
            return coinsCounts[amount]
        else:
            return -1

sol = Solution()
coins = [1, 2, 5]
amount = 11
assert sol.coinChange(coins, amount) == 3
coins = [1]
amount = 0
# print(sol.coinChange(coins, amount))
assert sol.coinChange(coins, amount) == 0