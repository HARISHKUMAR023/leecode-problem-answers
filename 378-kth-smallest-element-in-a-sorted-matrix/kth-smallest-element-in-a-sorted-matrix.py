class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        my=[]

        for i in range(1,len(matrix)):
            matrix[0].extend(matrix[i])
        s=sorted(matrix[0])
        return s[k-1]