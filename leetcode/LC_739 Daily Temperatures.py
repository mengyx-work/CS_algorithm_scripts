class Solution(object):
    def dailyTemperatures(self, T):
        res = {}
        stack = []
        for i in range(len(T)):
            print('start ', i, stack, res)
            while stack and T[stack[-1]] < T[i]:
                res[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
            # print('end ', i, stack, res)
        for i in stack:
            res[i] = 0
        return [res[i] for i in range(len(T))]

    # def dailyTemperatures(self, T):
    #     idxMap, res = {}, []
    #     for i in range(len(T)-1, -1, -1):
    #         days, cur = 0, i+1
    #         while cur < len(T):
    #             if T[cur] > T[i]:
    #                 days = cur - i
    #                 idxMap[i] = cur
    #                 break
    #             elif cur in idxMap:
    #                 cur = idxMap[cur]
    #             else:
    #                 cur += 1
    #         res.append(days)
    #     return res[::-1]

sol = Solution()
T = [73, 74, 75, 71, 69, 72, 76, 73]
print(sol.dailyTemperatures(T))

