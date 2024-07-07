class Solution {
    public int longestOnes(int[] nums, int k) {
        int left =0;
        int max_len=0;
        int c_zero = 0;
        for(int right =0 ; right < nums.length ; right++ ){
            if (nums[right] == 0){
               c_zero += 1;
            }
            while (c_zero > k){
               if (nums[left] == 0){
                    c_zero -=1;
               }
               left +=1;
               

            }
          
            max_len=Math.max(max_len,right - left+1);  
        }
        return max_len;
    }
}