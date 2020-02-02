class Solution(object):
    def monotoneIncreasingDigits(self, N):
        N = str(N)
        s, i = [], 0
        while i < len(N):
            chr = N[i]
            if len(s) == 0:
                s.append(chr)
                i += 1
            elif chr >= s[-1]:
                s.append(chr)
                i += 1
            else:
                i -= 1
                while i > 0:
                    if (int(s[i]) - 1) >= int(s[i-1]):
                        break
                    i -= 1
                break
        if i == len(N):
            return int(N)
        res = s[:i]
        res.append(str(int(s[i])-1))
        for _ in range(len(N) - i - 1):
            res.append('9')
        return int(''.join(res))

sol = Solution()
N = 10
assert sol.monotoneIncreasingDigits(N) == 9
N = 332
assert sol.monotoneIncreasingDigits(N) == 299
N = 1234
# print(sol.monotoneIncreasingDigits(N))
assert sol.monotoneIncreasingDigits(N) == 1234

