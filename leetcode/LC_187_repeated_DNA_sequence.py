class Solution:
   # @param {string} s
   # @return {string[]}
	def findRepeatedDnaSequences(self, s):
		if len(s)<10:
			return []

		seqnDict = {}
		repSeqn = set([])
		#print 's length: ', len(s)
		for i in range(len(s)-9):
			#print 'checking s[i:i+10]: ', s[i:i+10]
			if s[i:i+10] not in seqnDict:
				seqnDict[s[i:i+10]] = 1
			else:
				seqnDict[s[i:i+10]] += 1
				repSeqn.add(s[i:i+10])

		return list(repSeqn)


solut = Solution()
data = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#data = "AAAAAAAAAAA"
print solut.findRepeatedDnaSequences(data)
