
class Solution(object):
    def _add_water(self, heightMap, i, j):
        boundary_height = min(heightMap[i-1][j], heightMap[i+1][j], heightMap[i][j-1], heightMap[i][j+1])
        if boundary_height > heightMap[i][j]:
            heightMap[i][j] = boundary_height
            return (boundary_height - heightMap[i][j])
        return 0

    def trapRainWater(self, heightMap):
        tot_water = 0
        add_water = True
        while not add_water:
            added_water = 0
            for i in range(1, len(heightMap) - 1):
                for j in range(1, len(heightMap[0]) - 1):
                    added_water += self._add_water(heightMap, i, j)
            tot_water += added_water
            if added_water == 0:
                add_water = False
        return tot_water


sol = Solution()
heightMap = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
print sol.trapRainWater(heightMap)