from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        # Initialize the prefix sum array with an extra 0 at the beginning
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        # Calculate the sum from index left to right using the prefix sum array
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
