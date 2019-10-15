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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        curHead = dummyHead
        for _ in range(m-1):
            curHead = curHead.next
        tail = curHead.next
        print 'tail: {}'.format(tail.val)
        pre, cur, nex = None, tail, None
        for _ in range(n - m + 1):
            # print 'cur: {}, nex: {}'.format(cur.val, nex.val)
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        # print "tail: {}".format(tail.val)
        printLinkedList(cur)
        # print 'cur: {}, nex: {}'.format(cur.val, nex.val)
        tail.next = cur
        curHead.next = pre
        return dummyHead.next


sol = Solution()
# head = builtLinkedListFromList([1,2,3,3,4,4,5])
# head = builtLinkedListFromList([2,2,2])
head = builtLinkedListFromList([1,2,3,4,5])
printLinkedList(sol.reverseBetween(head, 2, 4))
head = builtLinkedListFromList([1,2,3,4,5])
printLinkedList(sol.reverseBetween(head, 2, 3))
head = builtLinkedListFromList([1,2,3,4,5])
printLinkedList(sol.reverseBetween(head, 2, 2))


