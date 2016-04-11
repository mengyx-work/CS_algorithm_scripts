class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def Factorial(self, m, n):
        term1 = 1
        for i in range(m+1, n+1):
            term1 *= i
        term2 = 1
        for i in range(1, n-m+1):
            term2 *= i
        return (term1/term2)
        
        
    def getRow(self, rowIndex):
        rowList = []
        for i in xrange(rowIndex+1):
            rowList.append(self.Factorial(i, rowIndex))
        return rowList


    def generate(self, numRows):

        rowList = []
        for k in xrange(numRows):
            row = self.getRow(k)
            rowList.append(row)
            print row

        return rowList


solut = Solution()
print solut.generate(5)
#print solut.getRow(4)
