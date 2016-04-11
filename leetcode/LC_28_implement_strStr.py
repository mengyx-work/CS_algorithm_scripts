class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        
        if len(needle)>len(haystack):
            return -1
            
        if len(needle)==0:
            return 0
            
        for i in range(len(haystack)-len(needle)+1):
            print 
            if needle==haystack[i:len(needle)+i]:
                return i
                
        return -1



solut = Solution()
print solut.strStr("mississippi", "issi")
