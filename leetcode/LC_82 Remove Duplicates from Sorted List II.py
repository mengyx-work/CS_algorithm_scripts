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
    def _getUniqueNode(self, curHead):
        # print('check: {}'.format(curHead.val))
        if curHead.next is None:
            return True, curHead

        curValue = curHead.val
        if curHead.next.val != curValue:
            return True, curHead

        while curHead is not None and curHead.val == curValue:
            curHead = curHead.next
        return False, curHead

    def deleteDuplicates(self, head):
        dummyHead = ListNode(0)
        dummyHead.next = head
        curHead = head
        curUniqueHead = uniqueHead = dummyHead
        while curHead is not None:
            isUnique, curHead = self._getUniqueNode(curHead)
            # print('get unique: {}'.format(curUniqueHead.next.val))
            if isUnique:
                curUniqueHead.next = curHead
                curHead = curHead.next
                curUniqueHead = curUniqueHead.next

        if curUniqueHead is not None:
            curUniqueHead.next = None
        return uniqueHead.next

sol = Solution()
# head = builtLinkedListFromList([1,2,3,3,4,4,5])
# head = builtLinkedListFromList([2,2,2])
head = builtLinkedListFromList([2,2,2,3,4])
printLinkedList(sol.deleteDuplicates(head))


