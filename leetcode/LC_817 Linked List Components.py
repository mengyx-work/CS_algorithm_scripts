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
    def numComponents(self, head, G):
        uniqueValues = set(G)
        counts = 0
        inSet = False
        # dummyHead = ListNode(0)
        # dummyHead.next = head
        # curHead = dummyHead
        curHead = head
        while curHead is not None:
            if curHead.val in uniqueValues:
                if not inSet:
                    counts += 1
                    inSet = True
            else:
                inSet = False
            curHead = curHead.next
        return counts

sol = Solution()
head = builtLinkedListFromList([0,1,2,3])
G = [0, 1, 3]
print sol.numComponents(head, G)
