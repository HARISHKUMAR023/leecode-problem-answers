class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        my={}
        ans=0
        for i in nums:
            my[i]=my.get(i,0)+1
        print(my)
        m=0
        for j in range(1,len(nums)+1):
            if j in my:    
                if my[j] == 2:
                    
                    ans=j
            else:
                    m=j
        return [ans,m]