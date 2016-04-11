class Solution:
    def backCaptrWord(self, s, wrdDic, lenList):
        for wrdLen in lenList:
            if wrdLen<=len(s):
                for word in wrdDic[wrdLen]:
                    if word==s[-wrdLen:]:
                        return True
        return False


	def captrWord(self, s, wrdDic, lenList, res, resList):
        #print ' the s: ', s
		for wrdLen in lenList:
			if wrdLen<=len(s):
				for word in wrdDic[wrdLen]:
					if word==s[0:wrdLen]:
						if len(s[wrdLen:])>0:
							self.captrWord(s[wrdLen:], wrdDic, lenList, word + ' ' + res, resList)
						else:
							resList.append(word + ' ' + res)
							return
                          
	'''
	## recursive search using the return list to collect/pass meta results ##
    def captrWord(self, s, wrdDic, lenList):
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

		self.captrWord(s, wrdDic, lenList, '', resList)

        if not self.backCaptrWord(s, wrdDic, lenList):
            return resList
        #resList = self.captrWord(s, wrdDic, lenList)
        return resList



solut = Solution()
s = "catsanddog"
dic = ["cat", "cats", "and", "sand", "dog"]
s = "aaaaaaa"
dic = ["aaaa","aa","a"]
#s= 'aa'
#dic = ['aa', 'a']
print solut.wordBreak(s, dic)

 

