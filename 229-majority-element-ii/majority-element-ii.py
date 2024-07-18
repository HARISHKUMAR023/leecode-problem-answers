class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        t=int(n/3)
        ans=[]
        my={}
        for i in nums:
            my[i]=my.get(i,0)+1
        for j,k in my.items():
            if k > t:
                ans.append(j)
        return ans
        