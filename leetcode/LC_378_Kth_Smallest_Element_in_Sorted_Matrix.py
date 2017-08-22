import math, heapq
class Solution(object):
    def findLowerBound(self, matrix, target):
        ''' helper function to find the 
        lowerBound value of any given target
        '''
        n, m = len(matrix), len(matrix[0])
        cur_row, cur_col = 0, m - 1
        lowBound = matrix[0][0]
        while(cur_row < n and cur_col >=0):
            if matrix[cur_row][cur_col] == target:
                return target

            if matrix[cur_row][cur_col] > target:
                cur_col -= 1
            else:
                lowBound = max(lowBound, matrix[cur_row][cur_col])
                cur_row += 1
        return lowBound

    def countByUpperBound(self, matrix, upperBound):
        '''count the number of element euqal or 
        smaller than the target value
        '''
        counter = 0
        n = len(matrix)
        for i in range(n):
            j = n - 1
            while(j >= 0 and matrix[i][j] > upperBound):
                j -= 1
            counter += j + 1
        return counter

    ## binary search on the value
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        lb, ub = matrix[0][0], matrix[n-1][n-1] 
        while (lb < ub):
            mid = lb + (ub - lb) / 2
            counter = self.countByUpperBound(matrix, mid)
            if counter < k:
                lb = mid + 1
            else:
                ub = mid
        return self.findLowerBound(matrix, lb)

    '''
    ## minHeap to store the top Kth elements
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        hq = []
        cur_row = 0
        ## push elements from first row to hq
        for cur_col in range(n):
            heapq.heappush(hq, (matrix[cur_row][cur_col], cur_row, cur_col))
        for counter in range(k-1):
            elem = heapq.heappop(hq)
            cur_row, cur_col = elem[1], elem[2]
            if cur_row < n-1:
                cur_row += 1
                heapq.heappush(hq, (matrix[cur_row][cur_col], cur_row, cur_col))
            else:
                continue
        elem = heapq.heappop(hq)
        return elem[0]
    '''


sol = Solution()

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
assert sol.kthSmallest(matrix, k) == 13

matrix = [[-5]]
k = 1
assert sol.kthSmallest(matrix, k) == -5

matrix = [[1,2],[1,3]]
k = 4
assert sol.kthSmallest(matrix, k) == 3

k = 1
assert sol.kthSmallest(matrix, k) == 1

matrix = [[1,2],[3,3]]
k = 3
assert sol.kthSmallest(matrix, k) == 3


matrix = [[1,3,5],[6,7,12],[11,14,14]]
k = 3
assert sol.kthSmallest(matrix, k) == 5


'''
    def findKthElement(self, k, nums1, nums2):
        counter = 0
        nums1Ptr, nums2Ptr = 0, 0
        while(nums1Ptr < len(nums1) and nums2Ptr < len(nums2)):
            counter += 1
            if nums1[nums1Ptr] <= nums2[nums2Ptr]:
                nums1Ptr += 1
                if counter == k:
                    return nums1[nums1Ptr-1]
            else:
                nums2Ptr += 1
                if counter == k:
                    return nums2[nums2Ptr-1]

        while(nums1Ptr < len(nums1)):
            counter += 1
            nums1Ptr += 1
            if counter == k:
                return nums1[nums1Ptr-1]

        while(nums2Ptr < len(nums2)):
            counter += 1
            nums1Ptr += 1
            if counter == k:
                return nums2[nums2Ptr-1]
        return -1
        

    def kthSmallest(self, matrix, k):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        sqrtK = int(math.sqrt(k))
        if sqrtK * sqrtK == k:
            return matrix[sqrtK-1][sqrtK-1]
        nums1 = matrix[sqrtK]
        nums2 = [matrix[i][sqrtK] for i in range(sqrtK)]
        print nums1, nums2, sqrtK
        return self.findKthElement(k-sqrtK*sqrtK, nums1, nums2)

    ## wrong solution
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        rowCount = k / n
        colCount = k % n
        #print rowCount, colCount
        if colCount != 0:
            return matrix[rowCount][colCount-1]
        else:
            return matrix[rowCount-1][n-1]
    '''

'''
## test the `findKthElement`
nums1 = [3, 3, 4, 5]
nums2 = [1, 2, 3]
assert sol.findKthElement(5, nums1, nums2) == 3

nums1 = [1, 2]
nums2 = [3, 3]
assert sol.findKthElement(3, nums1, nums2) == 3
'''


