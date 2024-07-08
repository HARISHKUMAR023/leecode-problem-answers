class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        # Initialize the maximum product, minimum product, and global maximum
        max_prod = min_prod = global_max = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                # Swap max_prod and min_prod if the current number is negative
                max_prod, min_prod = min_prod, max_prod

            # Update max_prod and min_prod
            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])

            # Update the global maximum product
            global_max = max(global_max, max_prod)

        return global_max
