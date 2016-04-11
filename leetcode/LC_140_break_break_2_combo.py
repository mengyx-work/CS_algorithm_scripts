class Solution:

    partSolutDict = {}

    def backCaptrWord(self, s, wrdDic, lenList):
        for wrdLen in lenList:
            if wrdLen<=len(s):
                for word in wrdDic[wrdLen]:
                    if word==s[-wrdLen:]:
                        return True
        return False

    #'''
    def captrWord(self, s, wrdDic, lenList, res, resList):
       
        #print ' the s: ', s
        for wrdLen in lenList:
            if wrdLen<=len(s):
                for word in wrdDic[wrdLen]:
                    if word==s[0:wrdLen]:
                        if len(s[wrdLen:])>0:
			    if len(res)>0:
                                #self.partSolutDict[s[:wrdLen]] = res+' '+word ## add the partial solution to the Dict ##
			        self.captrWord(s[wrdLen:], wrdDic, lenList, res+' '+word, resList)
			    else:
				self.captrWord(s[wrdLen:], wrdDic, lenList, word, resList)

                        else:
				if len(res)>0:
				    resElem = res + ' ' + word
				else:
				    resElem = word
					
				resList.append(resElem)
				return

    #'''
    
    '''
    ## recursive search using the return list to collect/pass meta results ##
    def captrWord(self, s, wrdDic, lenList):
        ## check whether the left string has been examed before ##
        if s in self.partSolutDict:
            return self.partSolutDict[s]

        #print ' the s: ', s
        tmpList = []
        for wrdLen in lenList:
            if wrdLen<=len(s):
                for word in wrdDic[wrdLen]:
                    if word==s[0:wrdLen]:
                        if len(s[wrdLen:])>0:
                            resList = self.captrWord(s[wrdLen:], wrdDic, lenList)
                            for res in resList:
                                #print 'res: ', res
                                tmpList.append(word + ' ' + res)
                            #print 'tmpList: ', tmpList
                        else:
                                tmpList.append(word)

        self.partSolutDict[s] = tmpList                        
        return tmpList
    '''    


    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        wrdDic = {}
        for word in wordDict:
            if len(word) in wrdDic:
                wrdDic[len(word)].append(word)
            else:
                wrdDic[len(word)] = [word]

        lenList = wrdDic.keys()
        lenList.sort()
        resList = []


        if not self.backCaptrWord(s, wrdDic, lenList):
            return resList

        ## use return list to collect all the cases ##
        #resList = self.captrWord(s, wrdDic, lenList)

        ## use a list resList to store all the results ##
        self.captrWord(s, wrdDic, lenList, '', resList)
        
        return resList


solut = Solution()
s = "catsanddog"
dic = ["cat", "cats", "and", "sand", "dog"]
s = "aaaaaaa"
dic = ["aaaa","aa","a"]

#s= 'aa'
#dic = ['aa', 'a']

#s = "ab"
#dic = ["a","b"]
print solut.wordBreak(s, dic)

 

