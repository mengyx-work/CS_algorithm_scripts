class Solution(object):
    def distributeCandies(self, candies):
        kind_dict = {}
        even_count = len(candies) // 2
        for candy in candies:
            if candy not in kind_dict:
                kind_dict[candy] = 1
            else:
                kind_dict[candy] += 1
        if len(kind_dict) > even_count:
            return even_count
        else:
            return len(kind_dict)

       
