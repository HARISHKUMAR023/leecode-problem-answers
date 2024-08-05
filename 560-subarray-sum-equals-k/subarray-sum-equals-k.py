class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
     my={0:1}
     presum =0 
     c=0
     for num in nums:
        presum+=num
        r=presum-k
        if r in my:
            c+=my[r]
        if presum in my:
            my[presum]+=1
        else:
            my[presum]=1
     return c

    
