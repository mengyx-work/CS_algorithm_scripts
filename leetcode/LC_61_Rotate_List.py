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
    def _getNodeBySteps(self, head, steps):
        curHead = head
        for _ in range(steps):
            curHead = curHead.next
        return curHead

    def rotateRight(self, head, k):
        N = 0
        curHead = head
        while curHead is not None:
            N += 1
            curHead = curHead.next

        if N == 0:
            return head

        k = k % N
        if k == 0:
            return head

        frontTail = self._getNodeBySteps(head, (N - k - 1))
        backFront = self._getNodeBySteps(head, (N - k))
        backTail = self._getNodeBySteps(head, (N - 1))
        backTail.next = head
        frontTail.next = None
        return backFront

sol = Solution()
head = builtLinkedListFromList([1,2,3,4])
printLinkedList(sol.rotateRight(head, 4))