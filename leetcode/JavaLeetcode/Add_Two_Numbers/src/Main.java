import java.util.ArrayList;
import java.util.List;

class Old_Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode headNode = null;
        ListNode curNode = null;
        int curValue = 0;
        while ((l1 != null) || (l2 != null)) {

            if (l1 != null) {
                curValue += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                curValue += l2.val;
                l2 = l2.next;
            }
            if (headNode == null) {
                headNode = new ListNode((curValue % 10));
                curNode = headNode;
            }
            else {
                curNode.next = new ListNode((curValue % 10));
                curNode = curNode.next;
            }
            curValue = ((curValue >= 10) ? 1 : 0);
        }

        if (curValue != 0) {
            curNode.next = new ListNode(curValue);
        }

//        ListNode.printListNodeContent(headNode, "final_result");
        return headNode;
    }
}


class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode curNode = dummyHead;
        int curValue = 0;
        while ((l1 != null) || (l2 != null)) {

            if (l1 != null) {
                curValue += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                curValue += l2.val;
                l2 = l2.next;
            }

            curNode.next = new ListNode((curValue % 10));
            curNode = curNode.next;
            curValue = ((curValue >= 10) ? 1 : 0);
        }

        if (curValue != 0) {
            curNode.next = new ListNode(curValue);
        }

        return dummyHead.next;
    }
}

public class Main {

    public static void main(String[] args) {
//        ListNode l1 = ListNode.createListNodeFromList(new int[]{1, 2, 3, 4});
        ListNode l1 = ListNode.createListNodeFromList(new int[]{1, 9});
        ListNode l2 = ListNode.createListNodeFromList(new int[]{2, 3, 4, 5});
//        ListNode.printListNodeContent(l1);
//        ListNode.printListNodeContent(l2);

        Solution solution = new Solution();
        ListNode res = solution.addTwoNumbers(l1, l2);
        ListNode.printListNodeContent(res, "final_result");

    }
}
