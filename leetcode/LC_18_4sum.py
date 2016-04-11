class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if len(nums)<4:
            return []

        SumDict = {}
        res = set([])
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                Sum = nums[i] + nums[j]
                #SumDict.append((Sum, (i, j)))
                if Sum in SumDict:
                    SumDict[Sum].append((i, j))
                else:
                    SumDict[Sum] = [(i, j)]
    
        sortList = sorted(SumDict.items(), key=lambda x: x[0])
        start = 0
        end = len(sortList) - 1
        #print sortList

        while start<=end:
            if (sortList[start][0] + sortList[end][0]) == target:
                for aSet in sortList[start][1]:
                    for bSet in sortList[end][1]:
                        unit = set([])
                        unit.add(aSet[0])
                        unit.add(aSet[1])
                        unit.add(bSet[0])
                        unit.add(bSet[1])
                        #print 'index: ', aSet[0], aSet[1], bSet[0], bSet[1]
                
                        if len(unit)==4:
                            unit = [ nums[indx] for indx in unit]
                            unit.sort()
                            #print 'unit result: ', unit
                            res.add(tuple(unit))

                start += 1
                end -= 1
                continue

            if (sortList[start][0] + sortList[end][0])>target:
                end -= 1

            if (sortList[start][0] + sortList[end][0])<target:
                start += 1

        return list(res)


solut = Solution()
#data = [-1, 2, 1, -4]
#data = [0 ,1, 2]
#data = [1, 0, -1, 0, -2, 2]
data = [0, 0, 0, 0]
data = [-3,-1,0,2,4,5]
data = [-3,-2,-1,0,0,1,2,3]
print solut.fourSum(data, 0)
