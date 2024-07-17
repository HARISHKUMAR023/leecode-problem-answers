/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
      let maxp = 0;
      let mini = prices[0];
        
        for (let i = 1; i < prices.length; i++) {  
            let c = prices[i] - mini;
            maxp = Math.max(maxp, c);
            mini = Math.min(mini, prices[i]);
        }
        
        return maxp;
};