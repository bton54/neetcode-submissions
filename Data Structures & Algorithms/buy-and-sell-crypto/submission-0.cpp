class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxP = 0; // max profit
        int bestPrice = prices[0]; // first day start

        // iterate through the prices
        // calculate as if we sold at that day and compare to max p
        // if we see a lower price, override best price to buy at 

        for (auto& price : prices) {
            
            
            maxP = max(maxP, price - bestPrice); 
            if (price < bestPrice) {
                bestPrice = price;
            }
        }

        return maxP;
    }
};
