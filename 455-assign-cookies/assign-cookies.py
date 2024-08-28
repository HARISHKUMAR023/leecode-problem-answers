class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l=0
        r=0
        while l < len(s):
            if g[r] <= s[l]:
                r+=1
            l+=1
            if r == len(g):
                break
        return r
            
            