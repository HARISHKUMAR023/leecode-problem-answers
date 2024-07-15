class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int index = 0; // Pointer for the next non-zero element

        // Move all non-zero elements to the front of the array
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                nums[index] = nums[i];
                index++;
            }
        }

        // Fill the remaining positions with zeros
        for (int i = index; i < n; i++) {
            nums[i] = 0;
        }
    }
};