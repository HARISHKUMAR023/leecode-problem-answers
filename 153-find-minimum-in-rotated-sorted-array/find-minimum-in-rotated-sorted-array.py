class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini=max(nums)
        for i in range(len(nums)):
            mini = min(mini,nums[i])
        return mini