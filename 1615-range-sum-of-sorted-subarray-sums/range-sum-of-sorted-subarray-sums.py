class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        lepw=[]
        for i in range(len(nums)):
            s=0
            for j in range(i , len(nums)):
                s+=nums[j]
                lepw.append(s)
        lepw.sort()
        
        return sum(lepw[left-1:right]) % (10**9 + 7)