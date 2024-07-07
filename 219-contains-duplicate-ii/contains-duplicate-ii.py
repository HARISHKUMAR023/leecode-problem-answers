class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in  range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and abs(nums[i]-nums[j]) <= k:
        #             return True
        #     return False
        index_map = {}  # Dictionary to store the latest index of each number
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                # If the number is already in the map and the distance is within k
                return True
            index_map[num] = i  # Update the latest index of the number
        return False