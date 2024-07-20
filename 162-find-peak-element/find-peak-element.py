class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for  i in range(0,len(nums)):
            if len(nums)==0:
                return 0
            if len(nums)-1 == i:
                return i 

            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                return i
        return 0