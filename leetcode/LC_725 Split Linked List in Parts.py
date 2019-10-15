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
    def splitListToParts(self, root, k):
        N = 0
        curHead = root
        while root is not None:
            N += 1
            root = root.next
        plusGroup = range((N % k))
        window = N // k
        res = []
        # print window, plusGroup
        ## assume the curHead is part of the current LinkedList
        for i in range(k):
            res.append(curHead)
            tmpCurHead = curHead
            steps = window - 1 if i not in plusGroup else window
            # print curHead.val, steps
            if steps > 0:
                for _ in range(steps):
                    tmpCurHead = tmpCurHead.next

            if tmpCurHead is not None:
                curHead = tmpCurHead.next
                tmpCurHead.next = None
        return res


sol = Solution()
head = builtLinkedListFromList([1,2,3,4])
sol.splitListToParts(head, 5)


