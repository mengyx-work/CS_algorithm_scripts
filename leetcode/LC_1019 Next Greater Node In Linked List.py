# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class DoubledLinkedListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
        self.createrValueNode = None


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
    valueList = []
    while curNode is not None:
        valueList.append(curNode.val)
        # print curNode.val
        curNode = curNode.next
    return valueList

def printDoubleLinkedListFromTail(tail):
    curNode = tail
    valueList = []
    while curNode is not None:
        valueList.append(curNode.val)
        # print curNode.val
        curNode = curNode.prev
    return valueList


# class Solution(object):
#     def _createDoubleLinkedList(self, head):
#         doubleLinkedListHead = DoubledLinkedListNode(head.val)
#         curDoubleNode = doubleLinkedListHead
#         curNode = head.next
#         while curNode is not None:
#             curDoubleNode.next = DoubledLinkedListNode(curNode.val)
#             tmpcurDoubleNode = curDoubleNode
#             curDoubleNode = curDoubleNode.next
#             curDoubleNode.prev = tmpcurDoubleNode
#             curNode = curNode.next
#         return doubleLinkedListHead, curDoubleNode
#
#     def getCreaterValueNode(self, curNode):
#         comparingNode = curNode.next
#         while comparingNode is not None and curNode.val >= comparingNode.val:
#             comparingNode = comparingNode.createrValueNode
#         if comparingNode is None:
#             return None
#         else:
#             return comparingNode
#
#     def nextLargerNodes(self, head):
#         """the current algorithm creates reversely
#         linked list and store the nextGreaterNode
#         to each node
#
#         :type head: ListNode
#         :rtype: List[int]
#         """
#         doubleLinkedListHead, doubleLinkedListTail  = self._createDoubleLinkedList(head)
#         # print("print list from tail: {}".format(printDoubleLinkedListFromTail(doubleLinkedListTail)))
#         results = []
#         curNode = doubleLinkedListTail
#         while curNode is not None:
#             createrValueNode = self.getCreaterValueNode(curNode)
#             curNode.createrValueNode = createrValueNode
#             if createrValueNode is None:
#                 results.append(0)
#             else:
#                 results.append(createrValueNode.val)
#             curNode = curNode.prev
#         return results[::-1]



def nextGreaterValue(elems):
    stack, res = [], []
    for i in range(len(elems)):
        res.append(0)
        while len(stack) > 0 and elems[stack[-1]] < elems[i]:
            res[stack.pop()] = elems[i]
        stack.append(i)
    print res
    print stack


nextGreaterValue([2,7,4,3,5])


class Solution(object):
    def nextLargerNodes(self, head):
        elems = []
        while head is not None:
            elems.append(head.val)
            head = head.next

        stack, res = [], []
        for i in range(len(elems)):
            res.append(0)
            while len(stack) > 0 and elems[stack[-1]] < elems[i]:
                res[stack.pop()] = elems[i]
            stack.append(i)
        return res

sol = Solution()

# inputList = [1, 4, 3, 2, 5, 2]
# outputList = [4, 5, 5, 5, 0, 0]
# head = builtLinkedListFromList(inputList)
# # print("linkedList: {}".format(printLinkedList(head)))
# assert sol.nextLargerNodes(head) == outputList
#
# inputList = [2,7,4,3,5]
# outputList = [7,0,5,5,0]
# head = builtLinkedListFromList(inputList)
# assert sol.nextLargerNodes(head) == outputList
#
# inputList = [2,1,5]
# outputList = [5,5,0]
# head = builtLinkedListFromList(inputList)
# assert sol.nextLargerNodes(head) == outputList
#
# inputList = [1,7,5,1,9,2,5,1]
# outputList = [7,9,9,9,0,5,0,0]
# head = builtLinkedListFromList(inputList)
# assert sol.nextLargerNodes(head) == outputList
# printLinkedList(reversedList)



