class Solution(object):
    def totalFruit(self, tree):
        counts, countDict = 0, {}
        start, maxLen = 0, 0
        for i in range(len(tree)):
            elem = tree[i]
            if elem not in countDict:
                countDict[elem] = 0
            if countDict[elem] == 0:
                counts += 1
            countDict[elem] += 1
            # print('end: ', i, counts, countDict)
            while counts > 2:
                startElem = tree[start]
                countDict[startElem] -= 1
                if countDict[startElem] == 0:
                    counts -= 1
                start += 1
            maxLen = max(maxLen, i - start + 1)
            # print('start: ', start, counts, countDict)
        return maxLen

sol = Solution()

# tree = [1,2,1]
# print(sol.totalFruit(tree))

tree = [1,2,1]
assert sol.totalFruit(tree) == 3
tree = [0,1,2,2]
assert sol.totalFruit(tree) == 3
tree = [1,2,3,2,2]
assert sol.totalFruit(tree) == 4
tree = [3,3,3,1,2,1,1,2,3,3,4]
assert sol.totalFruit(tree) == 5