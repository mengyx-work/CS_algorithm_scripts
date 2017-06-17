class Solution(object): 
    def hammingDistance(self, x, y):
        xStr = list('{:b}'.format(x))
        yStr = list('{:b}'.format(y))
        count= 0
        print xStr, yStr
        while xStr or yStr:
            x = xStr.pop() if xStr else '0'
            y = yStr.pop() if yStr else '0'
            if x != y:
                count += 1
        return count

sol = Solution()
assert sol.hammingDistance(1, 4) == 2
print sol.hammingDistance(3, 4)
        



