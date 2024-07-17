class Solution {
    public int maxProfit(int[] prices) {
      int maxp = 0;
        int mini = prices[0];
        
        for (int i = 1; i < prices.length; i++) {  
            int c = prices[i] - mini;
            maxp = Math.max(maxp, c);
            mini = Math.min(mini, prices[i]);
        }
        
        return maxp;
    }
}