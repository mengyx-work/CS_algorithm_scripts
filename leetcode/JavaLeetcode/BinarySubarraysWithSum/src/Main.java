import java.util.ArrayList;

class Solution {
    public int numSubarraysWithSum(int[] A, int S) {
        // case when S is 0, all the 0s segments
        if (S==0) {
            int numSubarrays = 0;
            int segmentCount = 0;
            for(int i=0; i<A.length; i++) {
                if (A[i] == 1) segmentCount = 0;
                else {
                    numSubarrays += 1;
                    numSubarrays += segmentCount;
                    segmentCount += 1;
                }
            }
            return numSubarrays;
        }

        /*
        for non-zero S, the index of 1s are used to define
        the boundary of star/end points.

        add additional index (-1, length) to address the corner
        index.
         */
        ArrayList<Integer> onesIndex = new ArrayList<>();
        onesIndex.add(-1);
        int numSubarrays = 0;
        int startOptions, endOptions;
        for(int i=0; i<A.length; i++) {
            if (A[i] == 1) onesIndex.add(i);
        }
        if (onesIndex.size() < S + 1) return numSubarrays;
        onesIndex.add(A.length);
        for (int i=1; i<(onesIndex.size() - S); i++) {
            startOptions = onesIndex.get(i) - onesIndex.get(i-1);
            endOptions = onesIndex.get(i+S) - onesIndex.get(i+S-1);
            numSubarrays += startOptions * endOptions;
        }
        return numSubarrays;
    }
}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
//        int[] array = new int[]{1,0,1,0,1};
        int[] array = new int[]{0,0,0,0,0};
        System.out.println(solution.numSubarraysWithSum(array, 0));
    }
}
