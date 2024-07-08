class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0
        while l < r:
             d=r-l
             m=min(height[l],height[r])
             f=d*m
             if res < f:
                res = f 
             elif height[l] > height[r]:
               r -=1
             else:
              l+=1
        return res
      