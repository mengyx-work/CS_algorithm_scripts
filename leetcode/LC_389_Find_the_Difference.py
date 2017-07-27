class Solution(object):
    def findTheDifference(self, s, t):
        if len(list(s)) == 0:
            return t
        t_chars, s_chars = list(t), list(s)
        char_map = {t_chars[0] : -1}
        for plus_char, minor_char in zip(s_chars, t_chars[1:]):
            if plus_char not in char_map:
                char_map[plus_char] = 0
            if minor_char not in char_map:
                char_map[minor_char] = 0
            char_map[plus_char] += 1
            char_map[minor_char] -= 1
        for char in char_map:
            if char_map[char] != 0:
                return char

sol = Solution()
print sol.findTheDifference('abcd', 'abcde')





