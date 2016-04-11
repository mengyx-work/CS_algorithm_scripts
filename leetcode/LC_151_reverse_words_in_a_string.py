class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if len(s)==0:
            return ""

        backPtr = len(s) - 1
        word = []
        newString = []
        while backPtr>=0:
            if s[backPtr]!=' ':
                word.append(s[backPtr])
            if s[backPtr]==' ' and len(word)!=0:
                newString.extend(word[::-1])
                newString.append(' ')
                word = []
            backPtr -= 1

        if (len(word))!=0:
            newString.extend(word[::-1])
        else:
            newString = newString[:-1]

        return ''.join(newString)


solut = Solution()
s = 'the sky is blue'
s = '1'
print solut.reverseWords(s)
                
