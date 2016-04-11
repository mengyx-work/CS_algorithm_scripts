class Solution:
	def wordBreak(self, s, wordDict):
		charaList = list(s)
		wordIndx = {word:0 for word in wordDict}
		results = set()
		for chara in charaList:
			for word in wordIndx:
				indx = wordIndx[word]
				if word[indx]==chara:
					wordIndx[word] += 1
				else:
					wordIndx[word] = 0

				if wordIndx[word]==(len(word)-1):
					results.add(word)
					wordIndx[word] = 0

		return list(results)


s = "lteetcoode"
#s = 'ab'
wordDict = ["leet", "code"]
#wordDict= ['a', 'b']
solut = Solution()
print solut.wordBreak(s, wordDict)


