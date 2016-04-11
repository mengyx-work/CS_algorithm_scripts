class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        numDict = {num:[] for num in range(1, 10)}
        zeroList = []
        for num in nums:
            strNum = str(num)
            if strNum=='0':
                zeroList.append(strNum)
            else:
                numDict[int(strNum[0])].append(strNum)

        resList = []
        for num in range(9, 0, -1):
            if len(numDict[num])>0:
                print numDict[num]
                maxLen = len(max(numDict[num], key=len))
                print 'maxLen: ', maxLen
                numList = []
                for elem in numDict[num]:
                    elemStr = str(elem)
                    #print 'the elem size: ', len(elem)
                    for i in range(maxLen-len(elem)):
                        elemStr +='0'
                    numList.append((elem, int(elemStr)))
                tmpList = sorted(numList, key=lambda x: x[1], reverse=True)
                print 'tmpList: ', tmpList                
                tmpList = [str(elem[0]) for elem in tmpList]
                resList.extend(tmpList)

        for zero in zeroList:
            resList.append(zero)
        return ''.join(resList)

                
          
solut = Solution()
data =  [3, 30, 34, 5, 9, 0]
print solut.largestNumber(data)
            
