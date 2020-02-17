class Solution(object):
    def reverseString(self, s):
        n = len(s) - 1

        for i in range(n/2+1):
            s[i], s[n-i] = s[n-i], s[i]
        return s

sol = Solution()
s = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
res = ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"]

assert sol.reverseString(s) == res