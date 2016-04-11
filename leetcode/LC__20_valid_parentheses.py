class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        str_dict = {'(':')', '{':'}', '[':']'}
        prnth = []
        for elem in s:
            if elem in str_dict:
                prnth.append(elem)
            else:
                if len(prnth)==0:
                    return False
                    
                if elem==str_dict[prnth[-1]]:
                    prnth.pop()
                else:
                    return False
        
        if len(prnth)!=0:
            return False
        else:
            return True
                    
        
solut = Solution()

print solut.isValid("{}")
