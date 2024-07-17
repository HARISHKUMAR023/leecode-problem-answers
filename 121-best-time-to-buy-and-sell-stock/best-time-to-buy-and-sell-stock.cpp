class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxp = 0;
        int mini = prices[0];
        
        for (int i = 1; i < prices.size(); i++) {  
            int c = prices[i] - mini;
            maxp = max(maxp, c);
            mini = min(mini, prices[i]);
        }
        
        return maxp;
    }
};