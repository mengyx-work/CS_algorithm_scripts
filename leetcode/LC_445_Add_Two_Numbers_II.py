class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        content = "{}".format(self.val)
        cur = self.next
        while cur is not None:
            content += "--> {}".format(cur.val)
            cur = cur.next
        return content
       
def build_linked_list(elem_list):
    if len(elem_list) == 0:
        return ListNode(None)
    head = ListNode(elem_list[0])
    cur = head
    for elem in elem_list[1:]:
        cur.next = ListNode(elem)
        cur = cur.next
    return head

def reverseList(head):
    cur, prev= head, None
    while cur is not None:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev

class Solution(object):
    def _reverse_linked_list(self, node):
        cur_node, prev_node = node, None
        while cur_node is not None:
            tmp = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = tmp
        return prev_node

    def addTwoNumbers(self, l1, l2):
        cur_l1, cur_l2 = self._reverse_linked_list(l1), self._reverse_linked_list(l2)
        dummy_l = ListNode(0)
        cur_l = dummy_l
        extra = 0
        while cur_l1 is not None or cur_l2 is not None:
            cur_sum = extra
            extra = 0
            if cur_l1 is not None:
                cur_sum += cur_l1.val
                cur_l1 = cur_l1.next
            if cur_l2 is not None:
                cur_sum += cur_l2.val
                cur_l2 = cur_l2.next
            if cur_sum > 9:
                cur_sum -= 10
                extra = 1
            cur_l.next = ListNode(cur_sum)
            cur_l = cur_l.next
        if extra > 0:
            cur_l.next = ListNode(extra)
        return self._reverse_linked_list(dummy_l.next)

def main():
    sol = Solution()
    #l1 = build_linked_list([1, 8])
    #l2 = build_linked_list([0])
    #print sol._reverse_linked_list(l2)
    #print sol.addTwoNumbers(l1, l2)
    #'''
    l1 = build_linked_list([7, 2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    print sol.addTwoNumbers(l1, l2)
#Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 8 -> 0 -> 7
    #l1 = build_linked_list([2, 4, 3])
    #l2 = build_linked_list([5, 6, 4])
    #'''
if __name__ == '__main__':
    main()
