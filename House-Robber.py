class Solution:
    def rob(self, nums: List[int]) -> int:
        # dynamic programming array
        dp = []
        # iterate over houses
        for i in range(len(nums)):
            if i==0:
                dp.append(nums[i])
            elif(i==1):
                current_val = max(nums[0],nums[1])
                dp.append(current_val)
            else:
                
                current_val = max(dp[i-1], dp[i-2]+nums[i])
                dp.append(current_val)
        return dp[-1]
