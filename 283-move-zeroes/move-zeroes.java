class Solution {
    public void moveZeroes(int[] nums) {
        int[] withoutzero = new int[nums.length];
        int[] withzero = new int[nums.length];
        int[] ans = new int[nums.length];
        int indexzero=0;
        int indexnonzero=0;
        for( int i=0 ; i<nums.length;i++){
            if (nums[i]==0){
                withzero[indexzero]=nums[i];
                indexzero+=1;
            }else{
              withoutzero[indexnonzero]=nums[i];
              indexnonzero+=1;
            }
        }
        // System.out.println(Arrays.toString(withoutzero));
        for (int j =0 ; j < nums.length;j++){
            nums[j]=withoutzero[j];
        }
      

    }
}