/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
        let maxi=nums[0];
        let sum = 0;
        for(let i =0 ; i<nums.length;i++){
            sum+=nums[i];
            if ( sum > maxi){
                maxi = sum;
            }
            if (sum < 0){
                sum=0;
            }

        }
        return maxi;
};