class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        g_ptr, s_ptr = 0, 0
        counter = 0
        while g_ptr < len(g) and s_ptr < len(s):
            if g[g_ptr] <= s[s_ptr]:
                counter += 1
                g_ptr += 1
                s_ptr += 1
                continue
            if g[g_ptr] > s[s_ptr]:
                s_ptr += 1
        return counter
g = [1, 2, 3]
s = [1, 1]
sol = Solution()
assert sol.findContentChildren(g, s) == 1
g = [1, 2]
s = [1, 2, 3]
assert sol.findContentChildren(g, s) == 2
g = []
assert sol.findContentChildren(g, s) == 0


