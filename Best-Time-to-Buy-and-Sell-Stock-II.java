class Solution {
    public int maxProfit(int[] prices) {  
        int profit = 0;
        int buy = 0;
        int sell = 0;
        while(sell < prices.length)
        {
            buy = dayBeforeNextIncrease(sell, prices);
            if(buy==-1){break;}
            sell = dayBeforeNextDrop(buy, prices);
            if(sell == -1){sell = prices.length-1;}
            System.out.println(buy+" "+ sell);
            profit+= prices[sell]-prices[buy];
            
        }
        return profit;
    }
    public int dayBeforeNextIncrease(int buy, int[] prices)
    {
        
        for(int i = buy+1; i < prices.length; i++)
        {
            if(prices[i]>prices[i-1])
            {
                return i-1;
            }
        }
        return -1;
    }
    public int dayBeforeNextDrop(int buy,int[] prices)
    {
     
        for(int i = buy+1; i < prices.length; i++)
        {
            if(prices[i]< prices[i-1])
            {
                return i-1;
            }
        }
        return -1;
    }
}
