class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def countPartitions(a, maxSum):
            n = len(a)  # size of array
            partitions = 1
            subarraySum = 0
            for i in range(n):
                if subarraySum + a[i] <= maxSum:
                    # insert element to current subarray
                    subarraySum += a[i]
                else:
                    # insert element to next subarray
                    partitions += 1
                    subarraySum = a[i]
            return partitions
        low = max(nums)
        high = sum(nums)
        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            partitions = countPartitions(nums, mid)
            if partitions > k:
                low = mid + 1
            else:
                high = mid - 1
        return low
    #    maxi=0
    #    start=0
    #    index=k
    #    while index <= len(nums):
    #         maxi = max(sum(nums[start:index]), maxi)
    #         start+=1
    #         index+=1
    #    return maxi