class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxi=max(nums)
        for i in range(maxi):
            if i not in nums:
                return i
        return maxi+1