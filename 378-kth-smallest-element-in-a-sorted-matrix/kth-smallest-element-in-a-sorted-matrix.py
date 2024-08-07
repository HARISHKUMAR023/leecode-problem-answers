class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        my=[]
        for i in matrix:
            for j in i:
                my.append(j)
        my.sort()
        return my[k-1]