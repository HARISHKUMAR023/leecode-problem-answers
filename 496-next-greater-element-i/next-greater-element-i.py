class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my={}
        for i in range(len(nums2)):
            my[nums2[i]] = i
        stack=[]
        for k in nums1:
            for s in range(my[k],len(nums2)):
                if k < nums2[s]:
                    stack.append(nums2[s])
                    break
            else:
                stack.append(-1)
        return stack


        # ans=[]
        # for i in range(len(nums1)):
        #     for j in range(i+1,len(nums2)):
        #         if nums1[i] < nums2[j]:
        #             ans.append(nums2[j])
        #             break
        #     else:
        #         ans.append(-1)
        # print(ans)
