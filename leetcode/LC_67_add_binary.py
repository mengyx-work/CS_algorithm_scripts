class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        aList = [int(x) for x in a] 
        bList = [int(x) for x in b]

        if len(aList)>=len(bList):
            bList = [0]*( len(aList) - len(bList)) + bList 
        else:
            aList = [0]*( len(bList) - len(aList)) + aList

        residual = 0
        result = []
        for a, b in zip(reversed(aList), reversed(bList)):
            if (a+b+residual)>=2:
                result.append(a+b+residual-2)
                residual = 1
            else:
                result.append(a+b+residual)
                residual = 0

        if residual==1:
            result.append(1)

        strNum = "".join(str(x) for x in reversed(result))

        return strNum


solut = Solution()
print solut.addBinary("11", "1")
                

