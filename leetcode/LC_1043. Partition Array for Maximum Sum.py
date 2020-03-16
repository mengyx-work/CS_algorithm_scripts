# class Solution(object):
#     def maxSumAfterPartitioning(self, A, K):
#         d = [0 for _ in range(len(A))]
#         d[0] = A[0]
#         for i in range(1, len(A)):
#             tmp = []
#             for j in range(K):
#                 if i < j:
#                     continue
#                 res = max(A[(i-j):(i+1)])*(j+1)
#                 if i >= (j+1):
#                     res += d[i-j-1]
#                 tmp.append(res)
#             d[i] = max(tmp)
#         # print(d)
#         return d[len(A)-1]


class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        d = [0 for _ in range(len(A))]
        for i in range(len(A)):
            cur = -float('inf')
            for k in range(K):
                if k > i:
                    continue
                cur = max(cur, A[i-k])
                if i-k-1 >= 0:
                    pre = d[i-k-1]
                else:
                    pre = 0
                # print('cur: ', cur, ' pre: ', pre)
                d[i] = max(d[i], pre+cur*(k+1))
                # print(i, k, d)
        return d[len(A)-1]


sol = Solution()
A = [1,15,7,9,2,5,10]
K = 3
print(sol.maxSumAfterPartitioning(A, K))