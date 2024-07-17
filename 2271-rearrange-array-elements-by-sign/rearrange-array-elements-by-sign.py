class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        nev=[]
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                nev.append(i)
        ans =[]
        for j in range(int(len(nums)/2)):
            ans.append(pos[j])
            ans.append(nev[j])
        return ans