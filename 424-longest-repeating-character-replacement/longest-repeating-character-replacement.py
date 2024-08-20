class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # left=0
        # right =0
        # for i in range:
        #     while left < right:
        #         s[left:right].count('A')
        l=0
        maxi_f=0
        max_len=0
        f={}
        for r in range(len(s)):
            f[s[r]]=f.get(s[r],0)+1
            maxi_f = max(maxi_f,f[s[r]])
            if (r-l+1) - maxi_f > k:
                f[s[l]]-=1
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len
 
            



        