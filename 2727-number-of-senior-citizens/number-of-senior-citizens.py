class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans=0
        for i in range(len(details)):
            if int(details[i][11:13]) > 60:
                ans+=1
        return ans