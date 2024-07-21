import java.util.Arrays;

class Solution {
    public int splitArray(int[] nums, int k) {
        int n = nums.length;  // size of array
        
        int low = Arrays.stream(nums).max().getAsInt();
        int high = Arrays.stream(nums).sum();
        
        while (low <= high) {
            int mid = (low + high) / 2;
            int partitions = countPartitions(nums, mid);
            if (partitions > k) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }
    
    private int countPartitions(int[] nums, int maxSum) {
        int partitions = 1;
        int subarraySum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (subarraySum + nums[i] <= maxSum) {
                subarraySum += nums[i];
            } else {
                partitions++;
                subarraySum = nums[i];
            }
        }
        return partitions;
    }
}
