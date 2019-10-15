

class Solution(object):
    def _containSubString(self, charDict):
        return all([elem <= 0 for elem in charDict.values()])

    def minWindow(self, s, t):
        start, minWindow = 0, None
        currentContent = t[:]
        charDict = {}
        for char in t:
            if char not in charDict:
                charDict[char] = 0
            charDict[char] += 1

        for i in range(len(s)):
            char = s[i]
            if char in charDict:
                charDict[char] -= 1
            # print('outside: ', start, i, charDict)

            while self._containSubString(charDict):
                # print(start, i, charDict)
                # print(start, i, s[start:(i+1)])
                if minWindow is None:
                    minWindow = s[start:(i+1)]
                elif len(minWindow) > (i - start + 1):
                    minWindow = s[start:(i + 1)]

                if s[start] in charDict:
                    charDict[s[start]] += 1
                start += 1

        if minWindow is None:
            return ''
        return minWindow

sol = Solution()
S = "ADOBECODEBANC"
T = "ABC"
print(sol.minWindow(S, T))



# class Solution:
#   # @param {string} s
#   # @param {string} t
#   # @return {string}
# 	def minWindow(self, s, t):
# 		if len(s)==0:
# 			return ""
#
# 		keyDict = {}
# 		for elem in t:
# 			if elem not in keyDict:
# 				keyDict[elem] = 1
# 			else:
# 				keyDict[elem] += 1
#
# 		fndKeys = {}
# 		start, end = 0, 0
# 		minWindow = s
# 		fndSolut = False
#
# 		for i in range(len(s)):
# 			## check if s[i] is in the right key ##
# 			if s[i] in keyDict and s[i] not in fndKeys:
# 				fndKeys[s[i]] = [i] ## first time, add the key to fndKeys ##
# 			elif s[i] in fndKeys: ## found before, update the index list ##
# 				if len(fndKeys[s[i]])==keyDict[s[i]]:
# 					fndKeys[s[i]].pop(0)
# 					fndKeys[s[i]].append(i)
# 				else:
# 					fndKeys[s[i]].append(i)
#
# 			## to set the proper start ##
# 			if len(fndKeys)==0:
# 				start += 1
# 				continue
#
# 			## to check if there's full match
# 			if len(fndKeys)==len(keyDict):
# 				matched = True
# 				for key in fndKeys:
# 					if len(fndKeys[key])!=keyDict[key]:
# 						matched = False
# 						break
#
# 				## full match if found, update the start point for the substring ##
# 				if matched:
# 					fndSolut = True
# 					while (s[start] not in fndKeys) or fndKeys[s[start]][0]>start:
# 						start += 1
#
# 					## update the minWindow ##
# 					if i-start<len(minWindow):
# 						minWindow = s[start:i+1]
# 						#print 'result substring: ', minWindow
#
# 					## remove the last and sensitive element ##
# 					if len(fndKeys[s[start]])==1:
# 						fndKeys.pop(s[start], None)
# 					else:
# 						fndKeys[s[start]].pop(0)
#
#
# 		if fndSolut:
# 			return minWindow
# 		else:
# 			return ""
#
#
# solut = Solution()
# #s = "ADOBECODEBANC"
# #target = "AABC"
# s = "a"
# target = "aa"
# target = 'a'
# print solut.minWindow(s, target)

				
				
		
