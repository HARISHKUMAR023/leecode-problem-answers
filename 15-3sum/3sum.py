class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                    
        return ans

            

        # st = set()
        # n=len(nums)
        # for i in range(n):
        #     hashset = set()
        #     for j in range(i + 1, n):
        #         # Calculate the 3rd element:
        #         third = -(nums[i] + nums[j])

        #         # Find the element in the set:
        #         if third in hashset:
        #             temp = [nums[i], nums[j], third]
        #             temp.sort()
        #             st.add(tuple(temp))
        #         hashset.add(nums[j])

        # ans = list(st)
        # return ans

        # ans=[]
        # for i in range(len(nums)):
        #     for j in range(i+1 , len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k]  ==0:            
        #                 if sorted([nums[i] ,nums[j] ,nums[k] ] ) not in  ans:
        #                      ans.append(sorted([nums[i] ,nums[j] ,nums[k] ] ))
        # return ans