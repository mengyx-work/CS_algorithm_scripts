class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []
        for chr in s:
            if stack and stack[-1][0] == chr:
                _, count = stack.pop()
                curCount = count + 1
                if curCount < k:
                    stack.append((chr, curCount))
            else:
                stack.append((chr, 1))
        res = []
        for chr, count in stack:
            for _ in range(count):
                res.append(chr)
        return ''.join(res)


sol = Solution()
s = "abcd"
k = 2
assert sol.removeDuplicates(s, k) == 'abcd'

s = "deeedbbcccbdaa"
k = 3
assert sol.removeDuplicates(s, k) == 'aa'

s = "pbbcggttciiippooaais"
k = 2
assert sol.removeDuplicates(s, k) == 'ps'
