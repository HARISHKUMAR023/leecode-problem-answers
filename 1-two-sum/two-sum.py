class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my:
                return my[complement], i
            my[nums[i]] = i