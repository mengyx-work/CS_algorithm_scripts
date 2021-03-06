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

class Solution(object):
    def reverseList(self, head):
        cur, prev= head, None
        while cur is not None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

head = build_linked_list([1, 2, 3])
print head
sol = Solution()
print sol.reverseList(head)

       
