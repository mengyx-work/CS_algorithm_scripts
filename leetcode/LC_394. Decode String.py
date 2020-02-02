class Solution(object):
    def decodeString(self, s):
        stack = []
        for e in s:
            if e == ']':
                subset = []
                while True:
                    chr = stack.pop()
                    if chr == '[':
                        break
                    else:
                        subset.append(chr)
                string = self.decodeString(''.join(subset[::-1]))
                digits = []
                while stack and stack[-1].isdigit():
                    digits.append(stack.pop())
                digits = int(''.join(digits[::-1]))
                fullStr = ''.join([string for _ in range(digits)])
                stack.append(fullStr)
            else:
                stack.append(e)
        return ''.join(stack)

sol = Solution()
s = "3[a]2[bc]"
assert sol.decodeString(s) == 'aaabcbc'
s = "3[a2[c]]"
assert sol.decodeString(s) == "accaccacc"
s = "2[abc]3[cd]ef"
assert sol.decodeString(s) == "abcabccdcdcdef"
