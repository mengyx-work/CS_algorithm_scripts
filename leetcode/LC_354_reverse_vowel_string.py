class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        head_pntr, tail_pntr = 0, len(s) - 1

        while (1):

            while(s[head_pntr] not in vowels):
                head_pntr += 1
                if head_pntr > tail_pntr or head_pntr > len(s) - 1:
                    break
            #print 'current head_pntr: ', head_pntr

            while(s[tail_pntr] not in vowels):
                tail_pntr -= 1
                if tail_pntr < head_pntr or tail_pntr < 0:
                    break
            #print 'current tail_pntr: ', tail_pntr

            if head_pntr < tail_pntr:
                s[head_pntr], s[tail_pntr] = s[tail_pntr], s[head_pntr]
                head_pntr += 1
                tail_pntr -= 1
            else:
                break

        return ''.join(s)


sol = Solution()

print sol.reverseVowels('Ui')
print sol.reverseVowels('leetcode')
print sol.reverseVowels('hello')


    
