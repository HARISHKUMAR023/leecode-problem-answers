class Solution:
    def thirdMax(self, nums: List[int]) -> int:
         p=sorted(nums)
         a=[]
         for i in p:
            if i not in a:
                 a.append(i)
       
         if len(a)== 2:
             return a[-1]
         elif len(a)==1:
             return a[0]
         else:
             return a[-3]