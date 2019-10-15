import java.util.HashSet;
import java.util.Set;

class Solution {
    boolean isSubstring(String S, String subString) {
        if (S.length() < subString.length()) return false;
        int subStringLength = subString.length();
        for (int i=0; i<=(S.length() - subStringLength); i++) {
            if (S.substring(i, i+subStringLength).equals(subString)) return true;
        }
        return false;

    }
    void addValidIntBySubtring(Set<Integer> validIntSet, String intStr) {
        for (int i=0; i<=intStr.length()-1; i++) {
            for (int j=i+1; j<=intStr.length(); j++) {
                validIntSet.add(Integer.parseInt(intStr.substring(i, j), 2));
            }
        }
    }

    public boolean queryString(String S, int N) {
        Set<Integer> validIntSet = new HashSet<>();
        for(int i=N; i>0; i--) {
            if (validIntSet.contains(i)) continue;
            String intStr = Integer.toBinaryString(i);
            if (!isSubstring(S, intStr)) {
//                System.out.println("found: " + intStr);
                return false;
            }
            addValidIntBySubtring(validIntSet, intStr);
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
//        System.out.println(solution.isSubstring("0110", "10"));
        System.out.println(solution.queryString("0110", 3));
        System.out.println(solution.queryString("0110", 4));

    }
}
