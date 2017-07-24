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
    def detectCycle(self, head):
        ptr_1, ptr_2 = head, head
        found_cycle = False
        while ptr_1.next is not None and ptr_2.next.next is not None:
            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next.next
            if ptr_1 == ptr_2:
                found_cycle = True
                break
        if not found_cycle:
            return None

        counter, ptr_2 = 0, head
        while ptr_1 != ptr_2:
            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next
        return ptr_1



head = build_linked_list([1, 1, 3, 4])
print head
