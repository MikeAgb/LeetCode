class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if(amount==0): return 0      
        dp = [math.inf]*(amount+1)
        min_val = min(coins)
      
        for i in range(amount+1):
                if(i==0): dp[i] = i
                if(i>= min_val):
                    
                    min_coins = math.inf
                    for coin in coins:
                        if(i-coin>=0):
                            min_coins = min(min_coins, dp[i-coin]+1)
                    dp[i] = min_coins
                            
        if(dp[amount] == math.inf): return -1            
        return dp[amount]
