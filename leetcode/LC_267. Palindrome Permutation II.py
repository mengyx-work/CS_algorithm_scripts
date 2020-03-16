from collections import Counter
class Solution(object):
    def dfs(self, m, res, s):
        if len(m.keys()) == 0:
            res.append(s)
        else:
            for char in m:
                cur_m = m.copy()
                cur_s = char + s + char
                cur_m[char] -= 2
                if cur_m[char] == 0:
                    cur_m.pop(char)
                self.dfs(cur_m, res, cur_s)

    def generatePalindromes(self, s):
        m = Counter(s)
        odd_char, res = None, []
        for char in m:
            if m[char] % 2 != 0:
                if odd_char is not None:
                    return []
                else:
                    odd_char = char

        if odd_char is not None:
            m[odd_char] -= 1
            if m[odd_char] == 0:
                m.pop(odd_char)
            self.dfs(m, res, odd_char)
        else:
            self.dfs(m, res, "")
        return res

sol = Solution()
s = "abb"
print(sol.generatePalindromes(s))