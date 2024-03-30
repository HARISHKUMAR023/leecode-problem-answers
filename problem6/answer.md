``` python 
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        st = s.split()
        ans=[]
        for i in range(0,k):
            ans.append(st[i])
        res=' ' .join(ans)
        return res

