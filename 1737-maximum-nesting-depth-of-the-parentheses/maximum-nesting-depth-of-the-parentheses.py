class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=[]
        c=0
        for  i in s:
            if i == "(":
              c+=1
            elif i == ")":
                maxi.append(c)
                c-=1
        if len(maxi) == 0:
            return 0
        
        return max(maxi)