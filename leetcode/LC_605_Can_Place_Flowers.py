class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        '''use the dummy head and tail element 0 to
        replace the corner case
        '''
        if len(flowerbed) < n:
            return False
        if len(flowerbed) == 1:
            if n==0 or (flowerbed[0] == 0 and n == 1):
                return True
            else:
                return False
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        for i in xrange(1, len(flowerbed)-1):
            if n == 0:
                return True
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        if flowerbed[-2] == 0 and flowerbed[-1] == 0:
            flowerbed[-1] = 1
            n -= 1
        if n <= 0:
            return True
        else:
            return False

sol = Solution()
flowerbed = [1]
assert sol.canPlaceFlowers(flowerbed, 0) == True
flowerbed = [1,0,0,0,1]
assert sol.canPlaceFlowers(flowerbed, 1) == True
flowerbed = [1,0,0,0,1]
assert sol.canPlaceFlowers(flowerbed, 2) == False
flowerbed = [0]
assert sol.canPlaceFlowers(flowerbed, 1) == True
flowerbed = []
assert sol.canPlaceFlowers(flowerbed, 1) == False

