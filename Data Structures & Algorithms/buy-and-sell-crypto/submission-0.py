class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Let's find the max profit by buying and selling.
        profit = 0

        # First "buy" an item.
        for i in range(len(prices)):

            # Now we can only sell that item on a later date (future indicies).
            for j in range(i + 1, len(prices)):
                
                # Calculate the difference in prices on a future date.
                # Take the maximum profit by testing the previous profits we've seen.
                profit = max(profit, prices[j] - prices[i])
            
        # Return the maximum profit we've made.
        return profit