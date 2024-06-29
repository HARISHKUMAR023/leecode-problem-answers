class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my={}
        m=[]
        for i in nums1:
            if i in nums2:
                m.append(i)
                nums2.remove(i)
                
        return m