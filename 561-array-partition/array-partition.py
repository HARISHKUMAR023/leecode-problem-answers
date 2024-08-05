class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        # Step 2: Initialize the sum
        total_sum = 0
        
        # Step 3: Sum up every second element (the minimums of pairs)
        for i in range(0, len(nums), 2):
            total_sum += nums[i]
        
        return total_sum
