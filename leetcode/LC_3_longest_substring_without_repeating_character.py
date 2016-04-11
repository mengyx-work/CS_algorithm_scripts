class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        charList = list(s)
        startIndex, maxLen = 0, 0
        charDict = {}
        print charList
        for i in range(len(charList)):
            if charList[i] not in charDict:
                charDict[charList[i]] = i
                
            else:
                print 'index %i is repeated, previous index: %i' % (i, charDict[charList[i]])
                if startIndex<=charDict[charList[i]]:
                    startIndex = charDict[charList[i]]+1
                    print 'change startIndex to: %i' % (startIndex)

                ##the index for repeated index is always up to date    
                charDict[charList[i]] = i
            
            print ('value i: %i, startIndex: %i') % (i, startIndex)
            length = i - startIndex + 1
            maxLen = max(maxLen, length)
            
        return maxLen



solut = Solution()
data = 'qwnfenpglqdq'
print solut.lengthOfLongestSubstring(data)
