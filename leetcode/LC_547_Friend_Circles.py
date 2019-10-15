from collections import deque

class Solution(object):
    def _find_cir_indx(self, M, i):
        if M[i][i] == 0:
            return []
        cirs = set([i])
        cur_idx = deque([i])
        while len(cur_idx) > 0:
            start = cur_idx.popleft()
            for j in range(start, len(M)):
                if M[start][j] == 1:
                    M[start][j] = 0
                    cur_idx.append(j)
                    cirs.add(j)
        return cirs

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        counts = 0
        for i in range(len(M)):
            cirs = self._find_cir_indx(M, i)
            if len(cirs) > 0:
                counts += 1
        return counts



data = [[1,1,0],
        [1,1,1],
        [0,1,1]]

sol = Solution()
assert sol.findCircleNum(data) == 1

data = [[1,1,0],
        [1,1,0],
        [0,0,1]]
assert sol.findCircleNum(data) == 2

data = [[1,0,0,1],
        [0,1,1,0],
        [0,1,1,1],
        [1,0,1,1]]

