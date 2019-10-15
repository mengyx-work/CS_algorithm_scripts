# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        dummyHead = ListNode(0)
        dummyHead.next = head
        curHead = dummyHead
        while curHead.next is not None and curHead.next.next is not None:
            resNodes = curHead.next.next.next
            node2 = curHead.next.next
            node1 = curHead.next
            curHead.next = node2
            node2.next = node1
            node1.next = resNodes
            curHead = curHead.next.next
        return dummyHead.next
