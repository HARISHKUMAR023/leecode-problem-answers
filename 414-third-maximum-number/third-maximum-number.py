class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))  
        unique_nums.sort(reverse=True)  
        if len(unique_nums) < 3:
            return unique_nums[0] 
        else:
            return unique_nums[2]  