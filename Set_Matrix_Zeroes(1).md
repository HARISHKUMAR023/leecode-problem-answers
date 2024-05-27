# 73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

 

Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1


``` python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        my=[]
        row=[]
        for i in range(len(matrix)):
            c=0
            for j in matrix[i]:
                if j == 0:
                    my.append(c)
                    row.append(i)
                c+=1


        for k in range(len(row)):
            
            for p in range(len(matrix)):
                y=0
                for l in matrix[p]:
                    if p == row[k]:
                        matrix[p][y]=0
                    y+=1
        
        for lp in my:
            for kp in range(len(matrix)):
                matrix[kp][lp]=0
```