class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = []
        c=0
        for i in nums:
            if i == 1:
                c+=1
            else:
                ans.append(c)
                c=0
        ans.append(c)
        return max(ans)