class Solution(object):
    def reverseWords(self, s):
        new_words = []
        words = s.split(' ')
        for word in words:
            new_word = word[::-1]
            new_words.append(new_word)
        return ' '.join(new_words)

sol = Solution()
s = "Let's take LeetCode contest"
assert sol.reverseWords(s) == "s'teL ekat edoCteeL tsetnoc"
