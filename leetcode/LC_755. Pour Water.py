class Solution(object):
    def pourWater(self, heights, V, K):
        for i in range(V):
            cur = K
            while cur > 0 and heights[cur-1] <= heights[cur]:
                cur -= 1
            while cur < len(heights)-1 and heights[cur] >= heights[cur+1]:
                cur += 1
            while cur > K and heights[cur-1] <= heights[cur]:
                cur -= 1
            heights[cur] += 1
        return heights

sol = Solution()
heights = [1,2,3,4,3,2,1,2,3,4,3,2,1]
V=5
K=2
# print(sol.pourWater(heights, V, K))
assert sol.pourWater(heights, V, K) == [3, 4, 4, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]

heights = [2,1,1,2,1,2,2]
V = 4
K = 3
assert sol.pourWater(heights, V, K) == [2,2,2,3,2,2,2]

heights = [1,2,3,4]
V = 2
K = 2
assert sol.pourWater(heights, V, K) == [2, 3, 3, 4]

heights = [3,1,3]
V = 5
K = 1
assert sol.pourWater(heights, V, K) == [4,4,4]
