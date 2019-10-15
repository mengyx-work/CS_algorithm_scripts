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
    def _collectValidSegment(self, head, k):
        curHead = head.next
        nodes = []
        for _ in range(k):
            if curHead is None:
                return []
            nodes.append(curHead)
            curHead = curHead.next
        return nodes

    def _createReversedLinkedList(self, nodes):
        print("len: {}".format(len(nodes)))
        dummyNode = ListNode(0)
        curNode = dummyNode
        for node in reversed(nodes):
            # print("node value: {}".format(node.val))
            curNode.next = node
            curNode = curNode.next
        curNode.next = None
        # print("PRINT LinkedList: {}".format(printLinkedList(dummyNode.next)))
        return dummyNode.next, nodes[0]

    def reverseKGroup(self, head, k):
        if k == 0:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        curHead = dummyHead
        while curHead is not None:
            nodes = self._collectValidSegment(curHead, k)
            if len(nodes) == 0:
                break
            restNode = nodes[-1].next
            segmentHead, segmentTail = self._createReversedLinkedList(nodes)
            curHead.next = segmentHead
            segmentTail.next = restNode
            curHead = segmentTail
        return dummyHead.next


sol = Solution()
head = builtLinkedListFromList([1,2,3,4,5])
printLinkedList(sol.reverseKGroup(head, 3))