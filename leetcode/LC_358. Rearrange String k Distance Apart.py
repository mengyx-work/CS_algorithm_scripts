from collections import defaultdict
class Solution(object):
    def rearrangeString(self, s, k):
        if k == 0:
            return s
        cnts = defaultdict(int)
        maxCnt = 0
        for char in s:
            cnts[char] += 1
            maxCnt = max(maxCnt, cnts[char])
        maxChars = []
        for char in cnts:
            if cnts[char] == maxCnt:
                maxChars.append(char)
        if ((maxCnt-1)*k + len(maxChars)) > len(s):
            return ""
        items = sorted(cnts.items(), key=lambda x: x[1], reverse=True)
        res = [None for _ in range(len(s))]
        idx = (len(s)-1) % k
        for char, cnt in items:
            for j in range(cnt):
                res[idx] = char
                idx += k
                if idx >= len(s):
                    idx = (idx - 1) % k
        return ''.join(res)

sol = Solution()
# s = "aabbcc"
# k = 3
# assert sol.rearrangeString(s, k) == 'acbacb'
s = "aabbccde"
k = 3
print(sol.rearrangeString(s, k))



