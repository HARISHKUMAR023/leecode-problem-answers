class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        
        // Step 1: Find the maximum number in the array
        int maxi = nums[0];
        for (int i = 1; i < n; i++) {
            if (nums[i] > maxi) {
                maxi = nums[i];
            }
        }
        
        // Step 2: Initialize found to -1 (indicating no number found yet)
        int found = -1;
        
        // Step 3: Check each number from 0 to maxi
        for (int j = 0; j <= maxi; j++) {
            boolean exists = false;
            for (int num : nums) {
                if (num == j) {
                    exists = true;
                    break;
                }
            }
            if (!exists) {
                found = j;
                break;
            }
        }
        
        // Step 4: If no missing number found up to maxi, the missing number is maxi + 1
        if (found == -1) {
            return maxi + 1;
        } else {
            return found;
        }
    }
}
