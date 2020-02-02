## https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
import collections

class Solution(object):
    def shortestSubarray(self, A, K):
        B, res = [0], len(A) + 1
        for i in range(len(A)):
            tot = A[i] + B[-1]
            B.append(tot)
        deq = collections.deque()
        for i in range(0, len(B)):
            while deq and B[i] - B[deq[0]] >= K:
                res = min(res, i - deq[0])
                deq.popleft()
            while deq and B[i] <= B[deq[-1]]:
                deq.pop()
            deq.append(i)
        if res == len(A) + 1:
            return -1
        return res



sol = Solution()
A = [84,-37,32,40,95]
K = 167
assert sol.shortestSubarray(A, K) == 3

A = [1,2]
K = 4
assert sol.shortestSubarray(A, K) == -1
# A = [1]
# K = 1
# print(sol.shortestSubarray(A, K))
# A = [1,2]
# K = 4
# print(sol.shortestSubarray(A, K))

# A = [2,-1,2]
# K = 3
# print(sol.shortestSubarray(A, K))
