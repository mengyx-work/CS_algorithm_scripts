class Solution:
    ## extend and fill the oneStack and zeroStack from adjacent points ##
    def fillStack(self, matrix, oneStack, zeroStack, x, y):
        vrtWidth = len(matrix)
        hrzWidth = len(matrix[0])

        if x-1>0:
            if matrix[x-1][y]=='0':
                zeroStack.append((x-1, y))
            else:
                oneStack.append((x-1, y))
        if y-1>0:
            if matrix[x][y-1]=='0':
                zeroStack.append((x, y-1))
            else:
                oneStack.append((x, y-1))

        if x+1<vrtWidth:
            if matrix[x+1][y]=='0':
                zeroStack.append((x+1, y))
            else:
                oneStack.append((x+1, y))
        if y+1<hrzWidth:
            if matrix[x][y+1]=='0':
                zeroStack.append((x, y+1))
            else:
                oneStack.append((x, y+1))


    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if len(matrix)==0:
            return 0
        
        '''
        try:
            hrzWidth = len(matrix[0])
        except TypeError:
            for elem in matrix:
                if elem=='1':
                    return 1
            return 0
        '''

        #print 'the matrix[0]:', matrix[0]

        vrtWidth = len(matrix)
        hrzWidth = len(matrix[0])

        ## only single list in the matrix ##
        #print 'hrzWidth: ', hrzWidth        
        if vrtWidth==1:
            for elem in matrix[0]:
                if elem=='1':
                    return 1
            return 0

        if hrzWidth==1:
            for elem in matrix:
                if elem=='1':
                    return 1
            return 0

        oneExit = False

        for row in range(vrtWidth):
            for col in range(hrzWidth):
                if matrix[row][col]=='1':
                    oneExit = True
                    #boundary = False
                    oneCount = 0
                    if row+1<vrtWidth:
                        if matrix[row+1][col]=='1':
                            oneCount += 1
                    else:
                        if matrix[row-1][col]=='0':
                            oneCount -= 1

                    if col+1<hrzWidth:
                        if matrix[row][col+1]=='1':
                            oneCount += 1
                    else:
                        if matrix[row][col-1]=='0':
                            oneCount -= 1

                    if row>0:
                        if matrix[row-1][col]=='1':
                            oneCount += 1
                    else:
                        if matrix[row+1][col]=='0':
                            oneCount -= 1

                    if col>0:
                        if matrix[row][col-1]=='1':
                            oneCount += 1
                    else:
                       if matrix[row][col+1]=='0':
                            oneCount -= 1

                    #print 'position: ', row, col, 'oneCount: ', oneCount
                    if oneCount<2:
                        #print 'special point: ', row, col
                        #matrix[row][col]='0'
                        tmpList = list(matrix[row])
                        tmpList[col] = '0'
                        matrix[row] = ''.join(tmpList)
                        
        #print 'matrix after removing irregualr 1: ', matrix

        ## there is not one element in the matrix ##
        if not oneExit:
            return 0

        visited = set([])
        zeroStack = []
        oneStack = []
        Stack = []
        point = (0, 0)
        if matrix[0][0]==0:
            zeroStack.append(point)
        else:
            oneStack.append(point)

        maxDiffX, maxDiffY = 0, 0
        nonEmpty = False

        ## check all the zeroStack and oneStack ##
        while len(zeroStack)!=0 or len(oneStack)!=0:

            while len(zeroStack)!=0:
                point = zeroStack.pop()
                if point not in visited:
                    x, y = point[0], point[1]
                    visited.add(point)
                    self.fillStack(matrix, oneStack, zeroStack, x, y)
      
 
            while len(oneStack)!=0:
                point = oneStack.pop()
                Stack=[]
                Stack.append(point)
                minX, minY = vrtWidth, hrzWidth
                maxX, maxY = 0, 0
                while len(Stack)!=0:
                    onePoint = Stack.pop()
                    if onePoint not in visited:
                        pointX, pointY = onePoint[0], onePoint[1]
                        visited.add(onePoint)
                        print 'using the point: ', pointX, pointY
                        print 'minX: %i, minY %i, maxX: %i, maxY: %i' % (minX, minY, maxX, maxY)
                        minX = min(minX, pointX)
                        minY = min(minY, pointY)
                        maxX = max(maxX, pointX)
                        maxY = max(maxY, pointY)
                        self.fillStack(matrix, Stack, zeroStack, pointX, pointY)
                        nonEmpty = True

                maxDiffY = max(maxDiffY, maxY-minY)
                maxDiffX = max(maxDiffX, maxX-minX)

        print 'maxDiffX and maxDiffY: ', maxDiffX, maxDiffY
        #return maxDiffX, maxDiffY
        if maxDiffX==0 or maxDiffY==0:
            if oneExit:
                return 1
            #print 'oneExit: ', oneExit
            else:
                return 0
        else:
            if maxDiffX<=maxDiffY:
                length = maxDiffX + 1
            else:
                length = maxDiffY + 1
            return (length*length)

solut = Solution()

#data = ["10100", "10111", "11111", "10010"]
#data = ["10100", "10111", "11101", "10010"]
data = ["0001","1101","1111","0111","0111"]
#data = ["10", "11", "01"]
#data =["1"]
#data = ["000"]
#data = ["00","00"]
#data = ["11", "11"]
#data =["01","10"]
#data = ["1101","1101","1111"]
print solut.maximalSquare(data)
