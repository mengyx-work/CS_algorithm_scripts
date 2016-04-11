class Solution:
    def moveStep(self, board, word, pnt, pntStack):
        pntX = pnt[0][0]
        pntY = pnt[0][1]
        indx = pnt[1]
        dirc = pnt[2]
        visited = pnt[3]
        if pntX>0 and dirc[3]:
            if board[pntX-1][pntY]==word[indx+1] and (pntX-1, pntY) not in visited:
                tmpVisited = visited[:]
                tmpVisited.append((pntX-1, pntY))
                pntStack.append(((pntX-1, pntY), indx+1, (1, 0, 1, 1), tmpVisited))
        if pntX+1<len(board) and dirc[1]:
            if board[pntX+1][pntY]==word[indx+1] and (pntX+1, pntY) not in visited:
                tmpVisited = visited[:]
                tmpVisited.append((pntX+1, pntY))
                pntStack.append(((pntX+1, pntY), indx+1, (1, 1, 1, 0), tmpVisited))
        if pntY>0 and dirc[2]:
            if board[pntX][pntY-1]==word[indx+1] and (pntX, pntY-1) not in visited:
                tmpVisited = visited[:]
                tmpVisited.append((pntX, pntY-1))
                pntStack.append(((pntX, pntY-1), indx+1, (0, 1, 1, 1), tmpVisited))
        if pntY+1<len(board[0]) and dirc[0]:
            if board[pntX][pntY+1]==word[indx+1] and (pntX, pntY+1) not in visited:
                tmpVisited = visited[:]
                tmpVisited.append((pntX, pntY+1))
                pntStack.append(((pntX, pntY+1), indx+1, (1, 1, 0, 1), tmpVisited))


        

    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, words):
        
        vrtWidth = len(board)
        if vrtWidth==0:
            return False

        hrzWidth = len(board[0])
        resList = []
        wrdDict = {}
        for word in words:
            if word[0] in wrdDict:
                wrdDict[word[0]].append(word)
            else:
                wrdDict[word[0]] = [word]

        for x in range(vrtWidth):
            for y in range(hrzWidth):
                pntStack = []
                if board[x][y] in wrdDict:
                    Dict = []
                    for word in wrdDict:

                    pntStack.append(((x, y), 0, (1, 1, 1, 1), [(x, y)]))

                while pntStack:
                    pnt = pntStack.pop()
                    if pnt[1]==(len(word)-1):
                        return True 
                    self.moveStep(board, word, pnt, pntStack)
        return False



solut = Solution()

#board = ["acccbaabba","bbaacabcac","cbcaababba","accccacccb","abaaaabbac","bababbcbab","aaacaabbcb","ccbaababcb","cacacaccba","abbbccbbaa","ababbacaac","ccbbaacaab","bbacaabcca","acbbcacbaa"]
#word = "aaacabbbbaccbb"

#board = ['aa']
#word = 'aaa'

#board = ['ABCE', 'SFCS', 'ADEE']
board = [['A'], ['B'], ['C']]

#word = 'ABCCED'
#word = 'ABCB'
word = 'ABC'


## element may repreat themselve ##
board = ["aaaa","aaaa","aaaa"]
word = "aaaaaaaaaaaaa"

print solut.exist(board, word)

