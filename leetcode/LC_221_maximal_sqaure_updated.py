import time

class Solution:
    
    def checkElemCndidate(self, matrix, row, col):

        if matrix[row][col]=='0':
            return False

        vrtWidth = len(matrix)
        hrzWidth = len(matrix[0])
        oneCount = 0

        if row+1<vrtWidth:
            if matrix[row+1][col]=='1':
                        oneCount += 1
        else:
          if matrix[row-1][col]=='0':
              return False

        if col+1<hrzWidth:
            if matrix[row][col+1]=='1':
                oneCount += 1
        else:
            if matrix[row][col-1]=='0':
                return False

        if row>0:
            if matrix[row-1][col]=='1':
                oneCount += 1
        else:
           if matrix[row+1][col]=='0':
               return False

        if col>0:
            if matrix[row][col-1]=='1':
                oneCount += 1
        else:
            if matrix[row][col+1]=='0':
                return False

        #print 'position: ', row, col, 'oneCount: ', oneCount
        if oneCount>=2 and oneCount<=3:
            return True
        elif oneCount==4:
            for x, y in zip((row-1, row-1, row+1, row+1), (col-1, col+1, col+1, col-1)):
                if matrix[x][y]!='0':
                    return True
        else:
            return False
            
    # @param x, y: the point coordinate
    # @param length: the length of square to test
    def checkLength(self, matrix, x, y, length):
        for i in range(length+1):
            for j in range(length+1):
                if matrix[x+i][y+j]=='0':
                    return False

        return True

    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if len(matrix)==0:
            return 0

        overall_start_time = time.time()

        vrtWidth = len(matrix)
        hrzWidth = len(matrix[0])

        ## only single list in the matrix ##
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

        cndtPoints =  set([])
        oneExit = False

        for row in range(vrtWidth):
            for col in range(hrzWidth):
                if matrix[row][col]=='1' and not oneExit:
                    oneExit = True
                if self.checkElemCndidate(matrix, row, col):
                    cndtPoints.add((row, col))

        if not oneExit:
            return 0
        elif len(cndtPoints)==0:
            return 1

        #print 'the candiates: ', cndtPoints
        maxLength = 0
        screen_point_time = time.time()
        for point in cndtPoints:
            x, y = point[0], point[1]
            length=1
            while x+length<vrtWidth and y+length<hrzWidth:
                #print 'point: ', x, y, 'check result: ',  self.checkLength(matrix, x, y, length) 
                if self.checkLength(matrix, x, y, length):
                    length += 1
                else:
                    break
            #print 'the length: ', length
            maxLength = max(maxLength, length)
        

        print("---from start to screen points %s seconds ---" % (screen_point_time - overall_start_time))
        print("---from screen point to the end  %s seconds ---" % (time.time() - screen_point_time))
        return maxLength**2



