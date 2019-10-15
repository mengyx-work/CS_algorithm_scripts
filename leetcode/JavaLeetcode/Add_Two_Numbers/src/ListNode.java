import java.util.ArrayList;
import java.util.List;

public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
    }

    public static void printListNodeContent(ListNode listNode, String message) {
        StringBuilder sb = new StringBuilder();
        sb.append(message).append(": ");
        while (listNode != null) {
//            System.out.printf(" %d ->", listNode.val);
            sb.append(" ").append(listNode.val).append(" ->");
            listNode = listNode.next;
        }
        System.out.println(sb.toString());
    }

    public static ListNode createListNodeFromList(int[] numList) {
        ListNode headNode = null;
        ListNode curNode = null;
        for(int num: numList) {

            if (headNode == null) {
                headNode = new ListNode(num);
                curNode = headNode;
            }
            else {
                curNode.next = new ListNode(num);
//                System.out.println(curNode.val);
                curNode = curNode.next;
            }
        }
        return headNode;
    }
}
