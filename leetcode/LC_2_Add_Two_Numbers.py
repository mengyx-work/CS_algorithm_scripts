# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#     def __repr__(self):
#         content = "{}".format(self.val)
#         cur = self.next
#         while cur is not None:
#             content += "--> {}".format(cur.val)
#             cur = cur.next
#         return content
#
# def build_linked_list(elem_list):
#     if len(elem_list) == 0:
#         return ListNode(None)
#     head = ListNode(elem_list[0])
#     cur = head
#     for elem in elem_list[1:]:
#         cur.next = ListNode(elem)
#         cur = cur.next
#     return head
#
# def reverseList(head):
#     cur, prev= head, None
#     while cur is not None:
#         tmp = cur.next
#         cur.next = prev
#         prev = cur
#         cur = tmp
#     return prev
#
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         cur_l1, cur_l2 = l1, l2
#         dummy_l = ListNode(0)
#         cur_l = dummy_l
#         extra = 0
#         while cur_l1 is not None or cur_l2 is not None:
#             cur_sum = extra
#             extra = 0
#             if cur_l1 is not None:
#                 cur_sum += cur_l1.val
#                 cur_l1 = cur_l1.next
#             if cur_l2 is not None:
#                 cur_sum += cur_l2.val
#                 cur_l2 = cur_l2.next
#             if cur_sum > 9:
#                 cur_sum -= 10
#                 extra = 1
#             cur_l.next = ListNode(cur_sum)
#             cur_l = cur_l.next
#         if extra > 0:
#             cur_l.next = ListNode(extra)
#         return dummy_l.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        resDummy = ListNode(0)
        head = resDummy
        cur = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                cur += l1.val
                l1 = l1.next
            if l2 is not None:
                cur += l2.val
                l2 = l2.next
            print(cur)
            head.next = ListNode(cur%10)
            head = head.next
            cur = cur / 10
        if cur != 0:
            head.next = ListNode(cur)
        return resDummy.next

sol = Solution()
l1 = build_linked_list([1, 8])
l2 = build_linked_list([0])
print(sol.addTwoNumbers(l1, l2))




       
