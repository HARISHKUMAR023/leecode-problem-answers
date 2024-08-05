class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int total_sum = 0 ;
        for ( int i =0 ; i < nums.length ; i+=2 ){
            total_sum += nums[i];


        }
        return total_sum;
    }
}