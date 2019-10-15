class Solution {
    public boolean isValid(String S) {
        while (S.length() > 0) {
            int oldLength = S.length();
            S = S.replace("abc", "");
            if (S.length() == oldLength) return false;
        }
        return true;
    }
}

public class Main {

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isValid("cababc"));
    }
}
