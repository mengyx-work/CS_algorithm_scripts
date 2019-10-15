import jdk.jshell.EvalException;

import java.util.Arrays;
import java.util.Comparator;

class LogComparator implements Comparator<String> {
    @Override
    public int compare(String log1, String log2) {
        int log1StartIndex = logStartIndex(log1);
        int log2StartIndex = logStartIndex(log2);
        if (log1.substring(log1StartIndex, log1StartIndex+1).matches("\\d+")) {
            if (log2.substring(log2StartIndex, log2StartIndex+1).matches("\\d+")) return 0;
            else return -1;
        }
        else {
            if (log2.substring(log2StartIndex, log2StartIndex+1).matches("\\d+")) return 1;
        }

    }

    int compareTwoStrings(String str1, String str2) {
        int i=0;
        int j=0;
        while (i<str1.length() && j<str2.length()) {
            if (str1.charAt(i) == str2.charAt(j)) {
                i++;
                j++;
            }
            else {
                if (str1.charAt(i) > str2.charAt(j)) return 1;
                else return -1;
            }
        }
    }


    int logStartIndex(String log) {
        for (int i=0; i<log.length(); i++) {
            if (log.substring(i, i+1).equals(" ")) return i+1;
        }
        throw new IllegalArgumentException("missing start");
    }

}

class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Arrays.sort(logs, LogComparator);
    }
}

public class Main {

    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
