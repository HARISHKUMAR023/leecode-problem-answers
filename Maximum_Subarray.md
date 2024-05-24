# 53. Maximum Subarray

Given an integer array nums, find the
subarray
with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


``` python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=0
        
        current_sum = max_sum = nums[0]

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Update the current sum by including the current number
            # or starting a new subarray with the current number
            current_sum = max(num, current_sum + num)
            # Update the max sum if the current sum is greater
            max_sum = max(max_sum, current_sum)
        
        return max_sum
            
      
```