/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
        ans = [];
 
       let  n =matrix.length;
       let m =matrix[0].length ;
    
        let top = 0;
        let left = 0;
        let bottom = n - 1;
        let right = m - 1;
       while (top <= bottom && left <= right) {

            // For moving left to right
            for (let i = left; i <= right; i++)
                ans.push(matrix[top][i]);

            top++;

            // For moving top to bottom.
            for (let i = top; i <= bottom; i++)
                ans.push(matrix[i][right]);

            right--;

            // For moving right to left.
            if (top <= bottom) {
                for (let i = right; i >= left; i--)
                    ans.push(matrix[bottom][i]);

                bottom--;
            }

            // For moving bottom to top.
            if (left <= right) {
                for (let i = bottom; i >= top; i--)
                    ans.push(matrix[i][left]);

                left++;
            }
        }
        return ans;
};