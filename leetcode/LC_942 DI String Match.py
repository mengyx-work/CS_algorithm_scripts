class Solution(object):
    def diStringMatch(self, S):
        levelList, curLevel = [(0, 0)], 0
        for i in range(len(S)):
            if S[i] == 'I':
                curLevel += 1
            else:
                curLevel -= 1
            levelList.append((curLevel, i + 1))

        levelList.sort(key=lambda x: x[0])
        results = list(range(len(S) + 1))
        for i in range(len(levelList)):
            _, index = levelList[i]
            results[index] = i
        return results

sol = Solution()
S = 'IDID'
print(sol.diStringMatch(S))
S = 'III'
print(sol.diStringMatch(S))
S = 'DDI'
print(sol.diStringMatch(S))

