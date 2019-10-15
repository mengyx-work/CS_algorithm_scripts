# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def builtLinkedListFromList(valueList):
    curNode = None
    for value in valueList:
        if curNode is None:
            curNode = ListNode(value)
            head = curNode
        else:
            curNode.next = ListNode(value)
            curNode = curNode.next
    return head


def printLinkedList(head):
    curNode = head
    vals = []
    while curNode is not None:
        vals.append(curNode.val)
        curNode = curNode.next
    print("LinkedList: {}".format(vals))
    return vals


class Solution(object):
    def reverseList(self, head):
        prev, curr, next = None, head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        i = 0
        curHead = head
        while curHead:
            i += 1
            curHead = curHead.next

        if (i % 2) == 0:
            n = i // 2
        else:
            n = i // 2 - 1

        curHead = head
        for _ in range(n):
            curHead = curHead.next

        secHead = self.reverseList(curHead.next)
        firHead = head
        curHead.next = None
        resDummyHead = ListNode(0)
        resHead = resDummyHead
        while firHead or secHead:
            if firHead:
                resHead.next = firHead
                firHead = firHead.next
                resHead = resHead.next
            if secHead:
                resHead.next = secHead
                secHead = secHead.next
                resHead = resHead.next
        return resDummyHead.next

sol = Solution()
head = builtLinkedListFromList([1, 2, 3, 4])
printLinkedList(sol.reorderList(head))