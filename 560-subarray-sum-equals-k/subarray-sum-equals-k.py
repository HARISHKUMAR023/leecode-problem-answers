class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      
       my = defaultdict(int)
       my[0] = 1  
       presum = 0
       cut = 0
       for i in range(len(nums)):
            presum += nums[i]
            r = presum - k
            cut += my[r]
            my[presum] += 1

       return cut
       