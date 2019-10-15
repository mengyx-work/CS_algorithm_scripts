class Solution(object):
    def smallestRange(self, nums):
        combinedList = []
        for i in range(len(nums)):
            for num in nums[i]:
                combinedList.append((num, i))
        combinedList.sort(key=lambda x: x[0])
        start, minRange = 0, float('inf')
        K, counts = len(nums), 0
        ans = None
        countDict = {}
        for i in range(K):
            countDict[i] = 0

        for i in range(len(combinedList)):
            num, index = combinedList[i]
            if countDict[index] == 0:
                counts += 1
            countDict[index] += 1

            while counts == K:
                start_num, start_index = combinedList[start]
                if num - start_num < minRange:
                    minRange = num - start_num
                    ans = (start_num, num)
                countDict[start_index] -= 1
                if countDict[start_index] == 0:
                    counts -= 1
                start += 1
        return ans
