/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
     let ans=[];
        let neg=1;
        let pos=0;
        for(let i =0 ; i<nums.length;i++){
            if (nums[i] > 0){
                ans[pos]=nums[i];
                pos+=2;
            }else{
                ans[neg]=nums[i];
                neg+=2;
            }
        }
            
        return ans;
};