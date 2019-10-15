import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] sortedSquares(int[] A) {
        int signChangeIndex = -1;
        for(int i=0; i<A.length-1; i++) {
            if (Integer.signum(A[i]) != Integer.signum(A[i+1])) {
                signChangeIndex = i;
                break;
            }
        }
        if (signChangeIndex == -1) {
            if (A[0] < 0) signChangeIndex = A.length - 1;
        }
        int i = signChangeIndex;
        int j = signChangeIndex + 1;
        ArrayList<Integer> tmpArray = new ArrayList<>();
        while (i >= 0 && j < A.length) {
            if (Math.abs(A[i]) > Math.abs(A[j])) {
                tmpArray.add(A[j] * A[j]);
                j++;
            }
            else {
                tmpArray.add(A[i] * A[i]);
                i--;
            }
        }
        if (i < 0) {
            while (j < A.length) {
                tmpArray.add(A[j] * A[j]);
                j++;
            }
        }
        if (j == A.length) {
            while (i >= 0) {
                tmpArray.add(A[i] * A[i]);
                i--;
            }
        }
        int[] sortedArrays = new int[A.length];
        for (int k=0; k<A.length; k++) sortedArrays[k] = tmpArray.get(k);
        return sortedArrays;
    }
}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
//        int[] array = new int[]{-4,-1,0,3,10};
//        int[] array = new int[]{-7,-3,2,3,11};
        int[] array = new int[]{2,3,8,11};
        System.out.println(Arrays.toString(solution.sortedSquares(array)));

    }
}
