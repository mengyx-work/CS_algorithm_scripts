class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead. 
    def solve(self, board):
        if len(board)==0:
            return 

        visited = set([])
        crsStack = []
        cirStack = []
        vrtWidth = len(board)
        hrzWidth = len(board[0])
        #print 'the start point: ', board[0][0]
        if board[0][0]=='X':
            crsStack.append((0, 0))
        else:
            cirStack.append((0, 0))


        while len(cirStack)!=0 or len(crsStack)!=0:

            while len(crsStack)!=0:
                point = crsStack.pop()
                x, y = point[0], point[1]
                
                if point not in visited:
                    visited.add(point)
                    if x+1<vrtWidth:
                        if board[x+1][y]=='X':
                            crsStack.append((x+1, y))
                        else:
                            cirStack.append((x+1, y))

                    if y+1<hrzWidth:
                        if board[x][y+1]=='X':
                            crsStack.append((x, y+1))
                        else:
                            cirStack.append((x, y+1))


            while len(cirStack)!=0:
                point = cirStack.pop()
                cndtStack = [] ## stack to store the possible 'X' points
                stack = [] ## stack to store the points to be modified
                #print point
                if point not in visited:
                    cndtStack.append(point)
                    NotBoudary = True

                    while cndtStack:
                        #print 'the cndtStack content: ', cndtStack
                        cirPoint = cndtStack.pop()
                        if cirPoint not in visited:
                            x = cirPoint[0]
                            y = cirPoint[1]
                            stack.append(cirPoint)
                            visited.add(cirPoint)

                            if x+1>=vrtWidth:
                                NotBoudary = False
                            else:
                                if board[x+1][y]=='X':
                                    crsStack.append((x+1, y))
                                else:
                                    cndtStack.append((x+1, y))
                            if x==0:
                                NotBoudary = False
                            else:
                                if board[x-1][y]=='X':
                                    crsStack.append((x-1, y))
                                else:
                                    cndtStack.append((x-1, y))
                            if y+1>=hrzWidth:
                                NotBoudary = False
                            else:
                                if board[x][y+1]=='X':
                                    crsStack.append((x, y+1))
                                else:
                                    cndtStack.append((x, y+1))
                            if y==0:
                                NotBoudary = False
                            else:
                                if board[x][y-1]=='X':
                                    crsStack.append((x, y-1))
                                else:
                                    cndtStack.append((x, y-1))



                if len(stack)!=0 and NotBoudary:
                    for x, y in stack:
                        #print 'position to change: ', x, y
                        chrList = list(board[x])
                        chrList[y]='X'
                        board[x] = ''.join(chrList)




solut = Solution()
#data = [['X','X', 'X', 'X'],['X','0', '0', 'X'], ['X','X', '0', 'X'], ['X','0', 'X', 'X']]
data = ["XOX","XOX","XOX"]
data = ["XXXX", "X00X", "XX0X", "X0XX"]
#data = ["OXXOX","XOOXO","XOXOX","OXOOO","XXOXO"]
solut.solve(data)
print data
