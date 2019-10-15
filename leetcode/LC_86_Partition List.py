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
    while curNode is not None:
        print curNode.val
        curNode = curNode.next

# class Solution(object):
#     def _getFirstNodeLargerThanX(self, curNode, x):
#         tmpCurNode = curNode
#         while tmpCurNode is not None and tmpCurNode.val < x:
#             tmpCurNode = tmpCurNode.next
#         return tmpCurNode
#
#     def _getFirstNodeSmallerThanX(self, curNode, x):
#         # if curNode is None:
#         #     return None
#         tmpCurNode = curNode
#         while tmpCurNode is not None and tmpCurNode.val >= x:
#             tmpCurNode = tmpCurNode.next
#         return tmpCurNode
#
#     def _swapNodeValue(self, node1, node2):
#         tmpValue = node1.val
#         node1.val = node2.val
#         node2.val = tmpValue
#
#     def partition(self, head, x):
#         curLargeNode = self._getFirstNodeLargerThanX(head, x)
#         curSmallNode = self._getFirstNodeSmallerThanX(curLargeNode.next, x)
#         print("start largeNode: {}".format(curLargeNode.val))
#         print("start smallNode: {}".format(curSmallNode.val))
#         while curSmallNode is not None and curLargeNode is not None:
#             # print("cur smallNode: {}, largeNode: {}".format(curSmallNode.val, curLargeNode.val))
#             self._swapNodeValue(curLargeNode, curSmallNode)
#             curLargeNode = self._getFirstNodeLargerThanX(curLargeNode, x)
#             curSmallNode = self._getFirstNodeSmallerThanX(curLargeNode, x)


class Solution(object):
    def partition(self, head, x):
        if head is None:
            return None
        curHead = head
        smallHead, largeHead = None, None
        while curHead is not None:
            if curHead.val < x:
                if smallHead is None:
                    smallHead = curHead
                    curSmallHead = smallHead
                else:
                    curSmallHead.next = curHead
                    curSmallHead = curSmallHead.next
            else:
                if largeHead is None:
                    largeHead = curHead
                    curLargeHead = largeHead
                else:
                    curLargeHead.next = curHead
                    curLargeHead = curLargeHead.next
            # print('current val: {}'.format(curHead.val))
            curHead = curHead.next

        if smallHead is None:
            return largeHead
        if largeHead is None:
            return smallHead
        curSmallHead.next = largeHead
        curLargeHead.next = None
        return smallHead

# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5

sol = Solution()

head = builtLinkedListFromList([1, 4, 3, 2, 5, 2])
# printLinkedList(head)
sol.partition(head, 3)
# printLinkedList(head)

head = builtLinkedListFromList([1])
sol.partition(head, 0)
printLinkedList(head)
