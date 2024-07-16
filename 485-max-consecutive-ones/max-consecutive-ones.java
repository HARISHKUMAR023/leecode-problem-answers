class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int c =0;
        int ans=0;
        for(int i =0;i<nums.length;i++){
            if (nums[i]==1){
                c+=1;
                if (c > ans){
                  ans = c;
            }
            }else{
                c=0;
            }
        }
        return ans;
    }
}