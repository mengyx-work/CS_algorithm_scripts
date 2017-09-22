class Solution:
    def twoSum(self, nums, target):
        numsDict = {i:elem for i, elem in zip(range(len(nums)), nums)}
        indxList = sorted(numsDict.items(), key=lambda x: x[1])
        indx1 = 0
        indx2 = len(nums)-1

        while indx1<indx2:
            if (indxList[indx1][1] + indxList[indx2][1])==target:
                print indxList[indx1][1], indxList[indx2][1]
                return (indxList[indx1][0]+1), (indxList[indx2][0]+1)

            if (indxList[indx1][1] + indxList[indx2][1])>target:
                indx2 -= 1

            if (indxList[indx1][1] + indxList[indx2][1])<target:
                indx1 += 1

solut = Solution()
data = [3, 2, 4]
print solut.twoSum(data, 6)
