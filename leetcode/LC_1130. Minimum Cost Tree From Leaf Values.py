class Solution(object):
    def mctFromLeafValues(self, arr):
        curSum = 0
        while len(arr) > 1:
            minIdx = arr.index(min(arr))
            neighbors = []
            if minIdx > 0:
                neighbors.append(arr[minIdx-1])
            if minIdx < (len(arr)-1):
                neighbors.append(arr[minIdx+1])
            minNeighbor = min(neighbors)
            curSum += minNeighbor*arr[minIdx]
            arr.pop(minIdx)
        return curSum

sol = Solution()
arr = [6,2,4]
print(sol.mctFromLeafValues(arr))

arr = [6,2,4,5,8]
print(sol.mctFromLeafValues(arr))