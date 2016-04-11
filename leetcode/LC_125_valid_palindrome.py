class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        
        strs = list(s.lower())
        
        if len(strs)<=1:
            return True
        
        startPtr = 0
        endPtr = len(strs)-1
        startChr = ''
        endChr = ''
        
        while endPtr>=startPtr:
            #print '{0}, {1}'.format(startPtr, endPtr)

            if (ord(strs[startPtr])>=97 and ord(strs[startPtr])<=122) or (ord(strs[startPtr])>=48 and ord(strs[startPtr])<=57):
                startChr = strs[startPtr]
            else:
                startPtr += 1
                startChr = ''
                continue
            
            if (ord(strs[endPtr])>=97 and ord(strs[endPtr])<=122) or  (ord(strs[endPtr])>=48 and ord(strs[endPtr])<=57) :
                endChr = strs[endPtr]
            else:
                endPtr -= 1
                endChr = ''
                continue

            #print '{0}, {1}'.format(startChr, endChr)
            
            if endChr!='' and startChr!='':
                
                if endChr==startChr:
                    startPtr += 1
                    endPtr -= 1

                else:
                    return False
                
        return True



solut = Solution()
print solut.isPalindrome('A man, a plan, a canal: Panama')
