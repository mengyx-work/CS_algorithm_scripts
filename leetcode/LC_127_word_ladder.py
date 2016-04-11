class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        '''
        for key in wordDict:
            for aKey in wordDict:
                if key!=aKey:
                    diff = 0
                    for char1, char2 in zip(key, aKey):
                        if char1!=char2:
                            diff += 1
                    if diff==1:
                        if key not in orderDict:
                            orderDict[key]=[aKey]
                        else:
                            orderDict[key].append(aKey)
        '''

        paths = [[beginWord]]
        foundNewPath = False
        resPaths = []

        while True:
            tmpPaths = []
            foundNewPath = False

            visitedWord = set([])
            for path in paths:
                for elem in path:
                    visitedWord.add(elem)
            #print 'visitedWord: ', visitedWord

            for path in paths:
                #print 'the path: ', path
                aKey = path[-1]
                wordDiff = 0
                ## check wit the endWord
                #print 'the last word, aKey: ', aKey
                for char1, char2 in zip(aKey, endWord):
                    if char1!=char2:
                        wordDiff += 1
                if wordDiff==1:
                    resPath = path[:]
                    resPath.append(endWord)
                    ## to collect all the possible paths and continue the search
                    #resPaths.append(resPath)
                    #foundNewPath = True
                    return len(resPath)

                else:
                    ## check with other words in the wordDict
                    for key in wordDict:
                        wordDiff = 0
                        for char1, char2 in zip(aKey, key):
                            if char1!=char2:
                                wordDiff += 1

                        if wordDiff==1:
                            if key not in visitedWord:
                                newPath = path[:]
                                #print 'the newPath: ', newPath
                                #print 'the visited words here: ', visitedWord
                                newPath.append(key)
                                tmpPaths.append(newPath)
                                foundNewPath = True
                            
            if foundNewPath:
                paths[:] = tmpPaths[:]
            elif len(resPaths)>0:
                break
            else:
                return -1
        
        minPathLen = len(wordDict)
        resPath = []
        for path in resPaths:
            #print 'path in the check loop: ', path
            if len(path)<minPathLen:
                minPathLen = len(path)
                resPath = path

        return minPathLen

solut = Solution()
wordDict = ["hot","dot","dog","lot","log"]
start = "hit"
end = "cog"
print solut.ladderLength(start, end, wordDict)
