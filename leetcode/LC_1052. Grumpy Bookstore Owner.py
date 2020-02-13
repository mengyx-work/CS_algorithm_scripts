class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        for i in range(len(grumpy)):
            if grumpy[i] > 0:
                customers[i] = -customers[i]
        idx, j = 0, 0
        maxCur, cur = 0, 0
        while j < len(customers):
            if customers[j] < 0:
                cur += customers[j]
            if j + 1 > X and customers[j-X] < 0:
                    cur -= customers[j-X]
            if cur <= maxCur:
                idx = j
                maxCur = cur
            j += 1
        for i in range(idx, idx-X, -1):
            print('i:', i)
            if customers[i] < 0:
                customers[i] = -customers[i]
        # print(idx, customers)
        return sum([elem for elem in customers if elem > 0])

sol = Solution()

# customers = [1,0,1,2,1,1,7,5]
# grumpy = [0,1,0,1,0,1,0,1]
# X = 3
# print(sol.maxSatisfied(customers, grumpy, X))

customers = [2,4,1,4,1]
grumpy = [1,0,1,0,1]
X = 2
print(sol.maxSatisfied(customers, grumpy, X))
