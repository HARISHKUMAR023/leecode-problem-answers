class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # brouteforce approch O(N2)
        # c=0
        # for i in range(len(nums)):
        #     sum=0
        #     for  j in range(i,len(nums)):
        #         sum+=nums[j]
        #         if sum == goal:
        #             c+=1
        # return c

        #optimal approach O(N)
        c=0
        s=0
        sum_dis={}
        sum_dis[0]=1
        for n in nums:
            s+=n
            if (s-goal)  in sum_dis:
                c+=sum_dis[s-goal]
            sum_dis[s]= sum_dis.get(s,0)+1
        return c
       

