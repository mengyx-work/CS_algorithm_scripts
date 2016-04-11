class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows==1:
            return s
        
        rows = [""]*numRows
        pttn_lngth = numRows*2 - 2
        resdul_nbr = len(s)%pttn_lngth
        pttn_nbr = (len(s) - resdul_nbr)/pttn_lngth

        resdul_str = s[(len(s)-resdul_nbr):]
        #pttn_str = s[:(len(s)-resdul_nbr)]
        if pttn_nbr>0:
            for i in xrange(pttn_nbr):
                for j in xrange(numRows):
                    if j==0 or j==(numRows-1):
                        rows[j] += s[i*pttn_lngth+j]
                    else:
                        rows[j] += s[i*pttn_lngth+j] + s[i*pttn_lngth+2*(numRows-1)-j]
        
        if resdul_nbr<=numRows:
            for k in xrange(resdul_nbr):
                rows[k] += resdul_str[k]
        else:

            for k in xrange(numRows):
                rows[k] += resdul_str[k]
            for k in xrange(resdul_nbr-numRows):
                rows[numRows-2-k] += resdul_str[k+numRows]
            for row in rows:
                print row
    
        result = ""
        for row in rows:
            result +=row
            
        return result
        
solut = Solution()
#print solut.convert("ABCDEFG", 3)
print solut.convert("ABCDEF", 4)
