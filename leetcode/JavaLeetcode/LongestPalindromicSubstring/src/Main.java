class Solution {
    public boolean isPalindromic(String s) {
        int start = 0;
        int end = s.length()-1;
        while (start <= end) {
            if(s.charAt(start) != s.charAt(end)) return false;
            start += 1;
            end -= 1;
        }
        return true;
    }
    public String longestPalindrome(String s) {
        if (s.equals("")) return s;
        int startIndex = 0;
        int endIndex = 1;
        for(int i=0; i<s.length()-1; i++) {
            for (int j=i + (endIndex - startIndex); j<=s.length(); j++) {
                if (isPalindromic(s.substring(i, j)) && (j-i)>(endIndex-startIndex)){
                    endIndex = j;
                    startIndex = i;
                }
            }
        }
        return s.substring(startIndex, endIndex);
    }
}

public class Main {

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.longestPalindrome("aaaaaa"));
    }
}
