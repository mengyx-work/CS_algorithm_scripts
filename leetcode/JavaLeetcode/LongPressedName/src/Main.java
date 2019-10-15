class Solution {
    public boolean isLongPressedName(String name, String typed) {
        int i=0;
        int j=0;
        char curChar = '\0';
        while (i<name.length()) {
            if (j >= typed.length()) return false;
            if (name.charAt(i) == typed.charAt(j)) {
                curChar = name.charAt(i);
                i++;
                j++;
            }
            else {
                if (typed.charAt(j) == curChar) j++;
                else return false;
            }
        }
        return true;
    }
}

public class Main {

    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
