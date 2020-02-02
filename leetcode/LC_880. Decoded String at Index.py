class Solution(object):
    def decodeAtIndex(self, S, K):
        charCounts = 0
        for i in range(len(S)):
            if S[i].isalpha():
                curCharCounts = charCounts + 1
                if curCharCounts == K:
                    return S[i]
            else:
                curCharCounts = int(S[i]) * charCounts
                if curCharCounts == K:
                    return self.decodeAtIndex(S[:i], charCounts)
                elif curCharCounts > K:
                    if K % charCounts == 0:
                        return self.decodeAtIndex(S[:i], charCounts)
                    return self.decodeAtIndex(S[:i], K % charCounts)
            charCounts = curCharCounts


sol = Solution()

S = "vk6u5xhq9v"
K = 554
assert sol.decodeAtIndex(S, K) == 'k'

S = "a23"
K = 6
assert sol.decodeAtIndex(S, K) == 'a'

S = "leet2code3"
K = 10
assert sol.decodeAtIndex(S, K) == 'o'

S = "a2345678999999999999999"
K = 1
assert sol.decodeAtIndex(S, K) == 'a'

S = "ha22"
K = 5
assert sol.decodeAtIndex(S, K) == 'h'

