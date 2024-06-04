# 229. Majority Element II

Medium
Topics
Companies
Hint

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]

Example 3:

Input: nums = [1,2]
Output: [1,2]

 

Constraints:

    1 <= nums.length <= 5 * 104
    -109 <= nums[i] <= 109


```
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        t=int(n/3)
        ans=[]
        my={}
        for i in nums:
            my[i]=my.get(i,0)+1
        for j,k in my.items():
            if k > t:
                ans.append(j)
        return ans
        
```