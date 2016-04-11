class Solution:
  # @param {character[][]} grid
  # @return {integer}
	def numIslands(self, grid):
		if len(grid)==0:
			return 0

		visited = set([])
		stack = []
		vrtWidth = len(grid)
		hznWidth = len(grid[0])
		start = (0, 0)
		curStack = []
		resStack = []
		if grid[0][0]=="1":
			curStack.append(start)
		else:
			resStack.append(start)

		islandCount = 0

		while len(curStack)!=0 or len(resStack)!=0:

			while len(curStack)!=0:
				point = curStack.pop()
				x, y = point[0], point[1]
                                Stack = []
				if point not in visited:
                                        islandCount += 1
                                        Stack.append(point)

                                        while Stack:
                                                ilndPnt = Stack.pop()
                                                #print 'the ilndPnt: ', ilndPnt
                                                if ilndPnt not in visited:
					                visited.add(ilndPnt)
                                                        ilndx, ilndy = ilndPnt[0], ilndPnt[1]

					                if ilndx+1<vrtWidth:
						                if grid[ilndx+1][ilndy]=="1":
							                Stack.append((ilndx+1, ilndy))
						                else:
							                resStack.append((ilndx+1, ilndy))

					                if ilndy+1<hznWidth:
						                if grid[ilndx][ilndy+1]=="1":
							                Stack.append((ilndx, ilndy+1))
						                else:
							                resStack.append((ilndx, ilndy+1))

                                                        if ilndx-1>=0:
                                                                if grid[ilndx-1][ilndy]=="1":
							                Stack.append((ilndx-1, ilndy))
						                else:
							                resStack.append((ilndx-1, ilndy))

                                                        if ilndy-1>=0:
                                                                if grid[ilndx][ilndy-1]=="1":
							                Stack.append((ilndx, ilndy-1))
						                else:
							                resStack.append((ilndx, ilndy-1))


			
			while len(resStack)!=0:
				point = resStack.pop()
				x, y = point[0], point[1]
				stat = grid[x][y]
				if point not in visited:
					visited.add(point)
					if x+1<vrtWidth:
						if grid[x+1][y]=="0":
							resStack.append((x+1, y))
						else:
							curStack.append((x+1, y))

					if y+1<hznWidth:
						if grid[x][y+1]=="0":
							resStack.append((x, y+1))
						else:
							curStack.append((x, y+1))



		return islandCount

solut = Solution()
data = ["1"]
data = ["010","111","010"]
print solut.numIslands(data)


