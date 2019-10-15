import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i=0; i < nums.length; i++) {
            int keyToCheck = target - nums[i];
            if (map.containsKey(keyToCheck)) {
                return new int[] {i, map.get(keyToCheck)};
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
public class Main {

    public static void main(String[] args) {
        int[] nums = {1, 3, 4, 5, 2};
        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.twoSum(nums, 5)));
    }
}
