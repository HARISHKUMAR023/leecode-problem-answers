class Solution {
    public int findPeakElement(int[] nums) {
        if (nums.length == 0) {
        return -1; 
    }

    if (nums.length == 1) {
        return 0; 
    }

    for (int i = 0; i < nums.length; i++) {
      
        if ((i == 0 || nums[i - 1] < nums[i]) && (i == nums.length - 1 || nums[i + 1] < nums[i])) {
            return i;
        }
    }

    return -1;
    }
}