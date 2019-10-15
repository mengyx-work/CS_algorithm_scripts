import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.HashSet;


//class Solution {
//    public int lengthOfLongestSubstring(String s) {
//        if ("".equals(s)) return 0;
//        String[] chars = s.split("");
//        int maxLength = 1;
//        for (int i=0; i<chars.length-1; i++) {
//            Set<String> charSet = new HashSet<>();
//            charSet.add(chars[i]);
//            int curLength = 1;
//            for (int j=i+1; j<chars.length; j++) {
//                if (charSet.contains(chars[j])) {
//                    break;
//                }
//                charSet.add(chars[j]);
//                curLength += 1;
//                if (curLength > maxLength) {
//                    maxLength = curLength;
//                }
//            }
//        }
//        return maxLength;
//    }
//}

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<String, Integer> indexMap = new HashMap<>();
        int ans = 0;
        for(int i =0, j=0; j < s.length(); j++) {
            if (indexMap.containsKey(s.charAt(j))){


            }

        }
    }
}

public class Main {

    public static void main(String[] args) {
//        System.out.println("Hello World!");
        Solution solution = new Solution();
        System.out.println(solution.lengthOfLongestSubstring("abccacbb"));

    }
}
