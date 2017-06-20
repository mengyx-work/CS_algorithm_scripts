class Solution(object): 
    def findComplement(self, num):
        numStr = list('{:b}'.format(num))
        reversed_num = []
        for num in numStr:
            if num == '1':
                reversed_num.append('0')
            else:
                reversed_num.append('1')
        return int(''.join(reversed_num), 2)
sol = Solution()
assert sol.findComplement(5) == 2
assert sol.findComplement(1) == 0

