class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

       left=0
       max_len=0
       c_zero=0
       for right in range(0,len(nums)):
           if nums[right] == 0:
            c_zero+=1
           while c_zero > k:
             if nums[left]==0:
                c_zero -=1
             left+=1
           max_len=max(max_len, right - left+1)
       return max_len