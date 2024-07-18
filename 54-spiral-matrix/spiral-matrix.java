class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        // ans = []
        List <Integer> ans = new ArrayList<>();
 
       int  n =matrix.length;
       int m =matrix[0].length ;
    
        int top = 0;
        int left = 0;
        int bottom = n - 1;
        int right = m - 1;
       while (top <= bottom && left <= right) {

            // For moving left to right
            for (int i = left; i <= right; i++)
                ans.add(matrix[top][i]);

            top++;

            // For moving top to bottom.
            for (int i = top; i <= bottom; i++)
                ans.add(matrix[i][right]);

            right--;

            // For moving right to left.
            if (top <= bottom) {
                for (int i = right; i >= left; i--)
                    ans.add(matrix[bottom][i]);

                bottom--;
            }

            // For moving bottom to top.
            if (left <= right) {
                for (int i = bottom; i >= top; i--)
                    ans.add(matrix[i][left]);

                left++;
            }
        }
        return ans;
    }
}