class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        if head is None:
            return head
        resHead = Node(0, None, None, None)
        curhead = resHead
        stack = [head]
        while len(stack) > 0:
            curNode = stack.pop()
            newNode = Node(curNode.val, curhead, None, None)
            curhead.next = newNode
            curhead = curhead.next
            if curNode.next is not None:
                stack.append(curNode.next)
            if curNode.child is not None:
                stack.append(curNode.child)
        res = resHead.next
        res.prev = None
        return res

