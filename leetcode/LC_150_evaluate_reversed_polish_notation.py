import operator

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        operators = {'/':lambda x, y: int(int(x)*1.0/int(y)), '*':lambda x, y: int(x)*int(y), '-':lambda x, y: int(x)-int(y), '+':lambda x, y: int(x)+int(y)}
        nums = []
        for token in tokens:
            if token in operators:
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(operators[token](num1, num2))
                print num1, num2, operators[token](num1, num2)
            else:
                nums.append(int(token))

        return nums[0]

    def recursive_evalRPN(self, tokens):

        operators = {'/':lambda x, y: int(int(x)/int(y)), '*':lambda x, y: int(x)*int(y), '-':lambda x, y: int(x)-int(y), '+':lambda x, y: int(x)+int(y)}
        
        if len(tokens)==1:
            return int(tokens[0])

        if (len(tokens)==3):
           return operators[tokens[2]](tokens[0], tokens[1])

        strs = []
        for i in range(0, len(tokens)-2):
            if (tokens[i] not in operators) and (tokens[i+1] not in operators) and (tokens[i+2] in operators):
                value = operators[tokens[i+2]](tokens[i], tokens[i+1])
                strs.append(str(value))
                strs.extend(tokens[i+3:])
                return self.evalRPN(strs)
            else:
                strs.append(tokens[i])


solut = Solution()
print solut.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
