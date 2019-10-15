class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''one-pass solution, use two pointers
    with a fixed distance.
    need to create a dummyHead to handle the case as [1]
    '''
    def removeNthFromEnd(self, head, n):
        dummyHead = ListNode(0)
        dummyHead.next = head
        front = dummyHead
        back = front
        for _ in range(n):
            front = front.next
        while front.next is not None:
            front = front.next
            back = back.next
        back.next = back.next.next
        return dummyHead.next