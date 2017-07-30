class MyQueue(object):
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)
        
    def pop(self):
        tmpList = []
        for i in xrange(len(self.data) - 1):
            tmpList.append(self.data.pop())
        result  = self.data.pop()
        self.data = tmpList[::-1]
        return result
        
    def peek(self):
        tmpList = []
        tot_len = len(self.data)
        for i in xrange(tot_len):
            tmp = self.data.pop()
            tmpList.append(tmp)
            if i == (tot_len - 1):
                self.data = tmpList[::-1]
                return tmp

    def empty(self):
        if len(self.data) > 0:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
obj = MyQueue()
nums = [1, 2, 3]
for num in nums:
    obj.push(num)
assert obj.pop() == 1
assert obj.peek() == 2
assert obj.empty() == False
obj.pop()
obj.pop()
assert obj.empty() == True

