class Solution {
public:
    int findPeakElement(vector<int>& nums) {
         if (nums.size() == 0) {
        return -1; 
    }

    if (nums.size() == 1) {
        return 0; 
    }

    for (int i = 0; i < nums.size(); i++) {
      
        if ((i == 0 || nums[i - 1] < nums[i]) && (i == nums.size() - 1 || nums[i + 1] < nums[i])) {
            return i;
        }
    }

    return -1;
    }
};