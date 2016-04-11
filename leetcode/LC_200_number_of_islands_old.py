class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if len(grid)==0 or len(grid[0])==0:
            return 0
        print len(grid), len(grid[0])    
        islndCount = 0
        vrtIslnd = False
        hrnIslnd = False
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if i-1>=0:
                    if int(grid[i-1][j])==1:
                        vrtIslnd = True
                    else:
                        vrtIslnd = False
                else:
                    vrtIslnd = False

                if j-1>=0:
                    if int(grid[i][j-1])==1:
                        hrnIslnd = True
                    else:
                        hrnIslnd = False
                else: 
                    hrnIslnd = False

                print hrnIslnd, vrtIslnd, type(grid[i][j])    
                if int(grid[i][j])==1 and hrnIslnd==False and vrtIslnd==False:
                    islndCount += 1
        
        return islndCount

solut = Solution()
grid = ["11"]
print solut.numIslands(grid)
