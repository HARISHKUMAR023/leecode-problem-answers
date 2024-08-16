class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # min_v=arrays[0][0]
        # max_v = arrays[0][-1]
        # maxi=0
        # for i in range(1,len(arrays)):
        #     cu_min=arrays[i][0]
        #     cu_max=arrays[i][-1]
        #     maxi=max(maxi,abs(min_v - cu_max), abs(max_v - cu_min))
        # min_v=min(min_v,cu_min)
        # mac_v=min(max_v, cu_max)
        # return maxi
            min_value = arrays[0][0]
            max_value = arrays[0][-1]
            max_distance = 0
            
            for i in range(1, len(arrays)):
                current_min = arrays[i][0]
                current_max = arrays[i][-1]
                
                # Calculate the maximum possible distance with the current array
                max_distance = max(max_distance, abs(current_max - min_value), abs(max_value - current_min))
                
                # Update min and max values for the next iteration
                min_value = min(min_value, current_min)
                max_value = max(max_value, current_max)
            
            return max_distance