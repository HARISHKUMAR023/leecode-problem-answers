class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_v = arrays[0][0]  # Initial minimum value from the first array
        max_v = arrays[0][-1]  # Initial maximum value from the first array
        maxi = 0  # To store the maximum distance
        
        for i in range(1, len(arrays)):
            cu_min = arrays[i][0]  # Current array's minimum value
            cu_max = arrays[i][-1]  # Current array's maximum value
            
            # Calculate the maximum distance considering the current array
            maxi = max(maxi, abs(min_v - cu_max), abs(max_v - cu_min))
            
            # Update min_v and max_v with the current array's values
            min_v = min(min_v, cu_min)
            max_v = max(max_v, cu_max)
        
        return maxi