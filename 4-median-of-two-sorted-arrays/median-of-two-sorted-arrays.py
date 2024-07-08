class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       new1=nums1
       for i in nums2:
           new1.append(i)
       new1.sort()
    
        
       if len(new1)%2!=0:
            a=int (len(new1)/2)
            return float(new1[a])
       else:
           c=int(len(new1)/2) 
           l=new1[c]+new1[c-1]
           return l/2   