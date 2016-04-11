from copy import deepcopy

class Solution:
    def FillpntStack(self, board, x, y, Dic, pntStack, dirc):
        vrtWidth = len(board)
        hrzWidth = len(board[0])
        tmpDic = deepcopy(Dic)
        #print 'bfr filling length: ', len(pntStack)
        if y>0 and dirc[2]:
            if board[x][y-1] in Dic:
                pntStack.append(((x, y-1), tmpDic, (0, 1, 1, 1)))
        if x>0 and dirc[3]:
            if board[x-1][y] in Dic:
                pntStack.append(((x-1, y), tmpDic, (1, 0, 1, 1)))
        if x+1<vrtWidth and dirc[1]:
            if board[x+1][y] in Dic:
                pntStack.append(((x+1, y), tmpDic, (1, 1, 1, 0)))
        if y+1<hrzWidth and dirc[0]:
            if board[x][y+1] in Dic:
                pntStack.append(((x, y+1), tmpDic, (1, 1, 0, 1)))
        #print 'afr filling length: ', len(pntStack)




    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        wrdDic = {}
        for s in word:
            if s not in wrdDic:
                wrdDic[s] = 1
            else:
                wrdDic[s] += 1

        vrtWidth = len(board)
        if vrtWidth==0:
            return 0

        hrzWidth = len(board[0])


        #print 'hrzWidth: ', hrzWidth
        #print 'wrdDic: ', wrdDic

        for row in range(vrtWidth):
            for col in range(hrzWidth):
                pntStack = []
                dirc = (1, 1, 1, 1)
                if board[row][col] in wrdDic:
                    curPnt = (row, col)
                    chkDic = deepcopy(wrdDic)
                    pntStack.append((curPnt, chkDic, dirc))
                #print 'new start point: ', pntStack
                while pntStack:
                    #print 'current pntStack: ', pntStack
                    elem = pntStack.pop()
                    x = elem[0][0]
                    y = elem[0][1]
                    letter = board[x][y]
                    Dic = elem[1]
                    dirc = elem[2]
                    #print 'checking point: ', x, y, 'the letter: ', letter, ' the Dic: ', Dic, 'direction: ', dirc
                    if letter in Dic:
                        Dic[letter] -= 1
                        if Dic[letter]==0:
                            Dic.pop(letter)
                    if len(Dic)==0:
                        return True
                    
                    self.FillpntStack(board, x, y, Dic, pntStack, dirc)


        return False



solut = Solution()

board = ["acccbaabba","bbaacabcac","cbcaababba","accccacccb","abaaaabbac","bababbcbab","aaacaabbcb","ccbaababcb","cacacaccba","abbbccbbaa","ababbacaac","ccbbaacaab","bbacaabcca","acbbcacbaa"]
word = "aaacabbbbaccbb"

#board = ['aa']
#word = 'aaa'

#board = ['ABCE', 'SFCS', 'ADEE']
#word = 'ABCCED'
#word = 'ABCB'
#word = 'ABC'

#board = [['A'], ['B'], ['C']]

print solut.exist(board, word)


                

 
