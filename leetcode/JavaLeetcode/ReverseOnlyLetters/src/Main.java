import java.util.HashMap;
import java.util.Stack;
import java.util.Map;

class Solution {
    public String reverseOnlyLetters(String S) {
        Stack charStack = new Stack();
        Map<Integer, Character> charMap = new HashMap<>();
        StringBuilder builder = new StringBuilder(S.length());

        for (int i=0; i<S.length(); i++) {
            if (Character.isLetter(S.charAt(i))) charStack.push(S.charAt(i));
            else charMap.put(i, S.charAt(i));
        }

        for (int i=0; i<S.length(); i++) {
            if (charMap.containsKey(i)) builder.append(charMap.get(i));
            else builder.append(charStack.pop());
        }
        return builder.toString();
    }
}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.reverseOnlyLetters("a-bC-dEf-ghIj"));
        System.out.println(solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"));

    }
}
