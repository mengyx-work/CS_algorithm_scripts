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

				if wordIndx[word]==(len(word)):
					results.add(word)
					wordIndx[word] = 0

		if len(results)==0 or len(wordIndx)==0:
			return False
		else:
			return True

s = "lteetcode"
wordDict = ["leet", "code"]
solut = Solution()
print solut.wordBreak(s, wordDict)


