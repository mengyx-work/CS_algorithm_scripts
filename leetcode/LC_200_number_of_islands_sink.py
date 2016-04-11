class Solution:
    def numIslands(self, grid):
        def sink(i, j):
            print 'sink check point: ', i, j
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1:
                grid[i][j] = 0
                points = map(lambda x, y: (x, y),  (i+1, i-1, i, i), (j, j, j+1, j-1))                
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                print 'points used in a mapping ', points 
                return 1
            return 0
        resList = [sink(i, j) for i in range(len(grid)) for j in range(len(grid[i]))]
        print resList
        return sum(resList)



solut = Solution()
data = ["1"]
data = [[0,1,0],[1,0,1],[0,1,0]]
print solut.numIslands(data)


