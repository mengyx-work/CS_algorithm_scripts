class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle)==1:
            return triangle[0][0]

        routine = [triangle[0][0]]
        minSum = triangle[0][0]
        SumList = [triangle[0][0]]
        lastIndx = 0
        lastDiff = [0]
        lastVal = []

        for layer in range(1, len(triangle)):
            
            if triangle[layer][lastIndx] > triangle[layer][lastIndx+1]:
                curIndx = lastIndx + 1
            else: curIndx = lastIndx
            
            ## the sum to compare with all other routine between two layers
            refSum =  triangle[layer][curIndx] + triangle[layer-1][lastIndx]
            curDiff = []

            ## layer+1 is also the element number ##            
            for i in range(layer+1):
                if i==0:
                    val = triangle[layer-1][i] + triangle[layer][i] - refSum + lastDiff[i]
                elif i==layer:
                    val = triangle[layer-1][i-1] + triangle[layer][i] - refSum + lastDiff[i-1]
                else:
                    val1 = triangle[layer-1][i-1] + triangle[layer][i]- refSum + lastDiff[i-1]
                    val2 = triangle[layer-1][i] + triangle[layer][i]- refSum + lastDiff[i]
                    val = min(val1, val2)
                curDiff.append(val)

            print 'layer: ', layer, 'curDiff: ', curDiff
            minDiff = min(curDiff) 
            curIndx = curDiff.index(minDiff)
            #print 'refSum: ', refSum
            minSum += minDiff + refSum - triangle[layer-1][lastIndx]

            lastIndx = curIndx
            lastDiff[:] = curDiff[:]
            routine.append(triangle[layer][curIndx])

        #return minSum, routine
        return minSum

solut = Solution()
data = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

data = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,4,3],
 [4,9,10,3,5]
]

data = [[-1],[2,3],[1,-1,-3]]

print solut.minimumTotal(data)




