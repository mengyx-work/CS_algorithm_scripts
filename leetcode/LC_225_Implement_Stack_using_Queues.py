import Queue
class MyStack(object):
    def __init__(self):
        self.data = Queue.Queue()

    def push(self, x):
        self.data.put(x)
        
    def pop(self):
        for i in xrange(self.data.qsize() - 1):
            tmp = self.data.get()
            self.data.put(tmp)
        return self.data.get()
        
    def top(self):
        for i in xrange(self.data.qsize()):
            tmp = self.data.get()
            self.data.put(tmp)
            if i == self.data.qsize() - 1:
                return tmp

    def empty(self):
        if self.data.qsize() > 0:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
nums = [1, 2, 3]
for num in nums:
    obj.push(num)
assert obj.pop() == 3
assert obj.top() == 2
assert obj.empty() == False
obj.pop()
obj.pop()
assert obj.empty() == True

