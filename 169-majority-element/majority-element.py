class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxin =nums[0]
        m=list(set(nums))
        for i in m:
            if nums.count(i) > 1:
              
               if nums.count(i) > nums.count(maxin):
                  maxin = i
        return maxin