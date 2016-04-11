class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle)==1:
            return triangle[0][0]

        SumList = [triangle[0][0]]
        minSum = min(SumList)
        
        for layer in range(1, len(triangle)):
            tmpSumList = [] 
            ## layer+1 is also the element number ##            
            for i in range(layer+1):
                if i==0:
                    val = SumList[i] + triangle[layer][i] 
                elif i==layer:
                    val = SumList[i-1] + triangle[layer][i]
                else:
                    val1 = SumList[i-1] + triangle[layer][i]
                    val2 = SumList[i] + triangle[layer][i]
                    val = min(val1, val2)
                tmpSumList.append(val)

            #print 'layer: ', layer, 'curDiff: ', curDiff
            SumList[:] = tmpSumList[:]
            minSum = min(SumList)

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
