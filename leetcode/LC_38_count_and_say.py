class Solution:
    def CountSay(self, initStr):
        Num = initStr[0]
        count = 1
        output = ""
        for i in range(1, len(initStr)):
            if initStr[i]== Num:
                count += 1
            else:
                output += str(count)+Num
                Num = initStr[i]
                count = 1
            
        output += str(count)+Num
        return output
        
        
    def countAndSay(self, n):
        if n==1:
            return "1"
            
        initStr = "1"
        seqn = ""
        seqn += initStr
        
        for i in range(1, n):
            output = self.CountSay(initStr)
            initStr = output
            #seqn += ", " + initStr

        #return seqn
        return initStr

solut = Solution()

print solut.countAndSay(4)
