# class Solution(object):
#     def kthSmallest(self, matrix, k):
#         n = len(matrix)
#         row_count = k / n
#         col_count = k % n
#         if col_count == 0:
#             return matrix[row_count][n-1]
#         else:
#             return matrix[row_count][col_count-1]

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        n, hq, visited = len(matrix), [], set()
        if k == 1:
            return matrix[0][0]
        heapq.heappush(hq, (matrix[0][0], 0, 0))
        for t in range(k-1):
            val, i, j = heapq.heappop(hq)
            # print(t, val, hq)
            if i+1 < n and (i+1, j) not in visited:
                heapq.heappush(hq, (matrix[i+1][j], i+1, j))
                visited.add((i+1, j))
            if j+1 < n and (i, j+1) not in visited:
                heapq.heappush(hq, (matrix[i][j+1], i, j+1))
                visited.add((i, j+1))
        val, _, _ = heapq.heappop(hq)
        # print('final: ', val)
        return val


class Solution(object):
    def kthSmallest(self, matrix, k):
        hq = []
        n = len(matrix)
        for i in range(n):
            heapq.heappush(hq, (matrix[0][i], 0, i))
        for _ in range(k-1):
            _, j, i = heapq.heappop(hq)
            if j < n - 1:
                heapq.heappush(hq, (matrix[j+1][i], j+1, i))
        return hq[0][0]

sol = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
# assert sol.kthSmallest(matrix, 2) == 5
# assert sol.kthSmallest(matrix, 8) == 13
assert sol.kthSmallest(matrix, 6) == 12

