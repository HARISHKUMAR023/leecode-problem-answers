/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
     let n = nums.length;
    let t = Math.floor(n / 3);
    let ans = [];
    let my = {};

    for (let i of nums) {
        my[i] = (my[i] || 0) + 1;
    }

    for (let j in my) {
        if (my[j] > t) {
            ans.push(parseInt(j));
        }
    }

    return ans;
};