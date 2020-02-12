# class Solution(object):
#     def baseNeg2(self, N):
#         if N == 0:
#             return '0'
#         if N > 0:
#             i = 0
#             maxN = pow(-2, 2*i)
#             while maxN < N:
#                 i += 1
#                 maxN += pow(-2, 2*i)
#             if pow(-2, 2*i) == N:
#                 return '1' + ''.join(['0' for _ in range(2*i)])
#             else:
#                 appendix = self.baseNeg2(N - pow(-2, 2*i))
#                 return '1' + ''.join(['0' for _ in range(2*i-len(appendix))]) + appendix
#         else:
#             j = 0
#             maxN = pow(-2, 2*j+1)
#             while maxN > N:
#                 j+=1
#                 maxN += pow(-2, 2 * j + 1)
#             if pow(-2, 2*j+1) == N:
#                 return '1' + ''.join(['0' for _ in range(2*j+1)])
#             else:
#                 appendix = self.baseNeg2(N - pow(-2, 2 * j+1))
#                 return '1' + ''.join(['0' for _ in range(2*j+1 - len(appendix))]) + appendix

class Solution(object):
    def base2(self, N):
        if N == 0:
            return 0
        res = ''
        while N != 0:
            if N % 2 == 0:
                res = '0' + res
            else:
                res = '1' + res
                N -= 1
            N = N / 2
        return res

    def baseNeg2(self, N):
        if N == 0:
            return 0

        res = ''
        while N != 0:
            if N % -2 == 0:
                res = '0' + res
            else:
                res = '1' + res
                N -= 1
            N = N / -2
        return res

sol = Solution()
print(sol.baseNeg2(-5))