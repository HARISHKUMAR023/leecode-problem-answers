class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans=[]
        a=["Gold Medal","Silver Medal","Bronze"]
        my={}
        c=1
        for i in score:
            my[i]=c
            c+=1
        # print(my)
        p=score
        p.sort(reverse = True)
        l=1
        for j in p:
            print(j)
            my[j]=l
            l+=1
        # print(my)
        ans=[]
        for k , p in my.items():
            if p == 1:
                ans.append("Gold Medal")
            elif p == 2:
                ans.append("Silver Medal")
            elif p == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(p))
        return ans