class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans=0
        for i in range(len(details)):
            n=details[i][11:13]
            if int(n) > 60:
                ans+=1
        return ans