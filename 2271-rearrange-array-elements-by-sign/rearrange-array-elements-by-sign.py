class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[0]* len(nums)
        neg=1
        pos=0
        for i in nums:
            if i > 0:
                ans[pos]=i
                pos+=2
            else:
                ans[neg]=i
                neg+=2
        return ans 