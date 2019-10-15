import org.jetbrains.annotations.NotNull;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

class CompareSet {
    private List<Map<Character, Integer>> wordMapList = new ArrayList<>();

    CompareSet(@NotNull String[] strings) {
        for (String word: strings) {
            this.wordMapList.add(convertWordToCharMap(word));
        }
    }

    private Map<Character, Integer> convertWordToCharMap(@NotNull String word) {
        Map<Character, Integer> charMap = new HashMap<>();
        for(int i=0; i<word.length(); i++) {
            char oneChar = word.charAt(i);
            if (charMap.containsKey(oneChar)) charMap.put(oneChar, charMap.get(oneChar) + 1);
            else charMap.put(oneChar, 1);
            }
        return charMap;
    }

    static boolean isSubsetWord(Map<Character, Integer> longCharMap, @NotNull Map<Character, Integer> shortCharMap) {
        for(char testChar: shortCharMap.keySet()) {
            if (!longCharMap.containsKey(testChar) || shortCharMap.get(testChar) > longCharMap.get(testChar)) {
//                System.out.println("failed to match " + shortCharMap + " with " + longCharMap);
                return false;
            }
        }
        return true;
    }

    public boolean isUniversalWord(String word) {
        Map<Character, Integer> charMap = convertWordToCharMap(word);
        for (int i=0; i<this.wordMapList.size(); i++) {
            if (!isSubsetWord(charMap, this.wordMapList.get(i))) {
                return false;
            }
        }
        return true;
    }
}
class Solution {
    public List<String> wordSubsets(String[] A, String[] B) {
        CompareSet compareSet = new CompareSet(B);
        List<String> universalWords = new ArrayList<>();
        for (String word : A) {
            if (compareSet.isUniversalWord(word)) universalWords.add(word);
        }
        return universalWords;
    }
}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] A = new String[]{"amazon","apple","facebook","google","leetcode"};
//        String[] B = new String[]{"e","o"};
        String[] B = new String[]{"ec","oc","ceo"};
        System.out.println(solution.wordSubsets(A, B));
    }
}
