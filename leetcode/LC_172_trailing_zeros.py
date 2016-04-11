class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        if(n/5==0):
            return 0
            
        result = 0 
        
        while (n/5)>0:
            result += n/5
            n = n/5
            print result

        return result


solut = Solution()
print 'function result: ', solut.trailingZeroes(200)
