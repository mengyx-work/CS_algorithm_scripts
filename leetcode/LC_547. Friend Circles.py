class Solution(object):
    def findCircleNum(self, M):
        cnts, n = 0, len(M)
        if n <= 1:
            return n
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            h = [i]
            cnts += 1
            while h:
                i = h.pop()
                visited.add(i)
                for j in range(n):
                    if j == i or j in visited or j in h or M[i][j] == 0:
                        continue
                    h.append(j)
        return cnts

sol = Solution()
M = [[1, 1, 0],
     [1, 1, 1],
     [0, 1, 1]]
assert sol.findCircleNum(M) == 1


M = [[1,0,0],[0,1,0],[0,0,1]]
assert sol.findCircleNum(M) == 3

M = [[1,1,0],
 [1,1,0],
 [0,0,1]]
assert sol.findCircleNum(M) == 2

