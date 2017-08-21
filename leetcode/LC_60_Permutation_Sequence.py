class Solution(object):
    @staticmethod
    def _get_factorial(n):
        res = 1
        for i in xrange(1, n+1):
            res *= i
        return res

    def getPermutation(self, n, k):
        num = []
        candidate_elems = [e for e in xrange(1, n+1)]
        for i in xrange(n, 0, -1):
            unit_iters = self._get_factorial(i-1)
            if k == 1:
                num.extend(candidate_elems)
                #return num
                return ''.join([str(e) for e in num])

            if unit_iters > k:
                num.append(candidate_elems.pop(0))
            else:
                counts = k / unit_iters
                k = k % unit_iters
                if k == 0:
                    num.append(candidate_elems.pop(counts-1))
                    candidate_elems = candidate_elems[::-1]
                    num.extend(candidate_elems)
                    #return num
                    return ''.join([str(e) for e in num])
                else:
                    num.append(candidate_elems.pop(counts))

sol = Solution()
assert sol.getPermutation(3, 1) == [1, 2, 3]
assert sol.getPermutation(3, 2) == [1, 3, 2]
assert sol.getPermutation(3, 3) == [2, 1, 3]
assert sol.getPermutation(3, 4) == [2, 3, 1]
assert sol.getPermutation(3, 6) == [3, 2, 1]

              


