/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let ans=[]
    let c=0
    for (let i=0;i<nums.length;i++){
        if (nums[i]==1){
            c+=1
        }else{
            ans.push(c)
            c=0
        }

    }
    ans.push(c)
    return Math.max(...ans)
};