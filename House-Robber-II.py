class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp1 = []
        dp2 = []
        if(len(nums)==1): return nums[0]
        if(not nums): return 0
        
        for i in range(len(nums)-1):
            if(i==0 or i==1):
                dp1.append(nums[0])
            else:
                dp1.append(max(dp1[i-1], dp1[i-2]+nums[i]))
                
        for i in range(1,len(nums)):
            if(i==1):
                dp2.append(nums[1])
            elif(i==2):
                dp2.append(max(nums[1],nums[2]))
            else:
               
                dp2.append(max(dp2[i-2],dp2[i-3]+nums[i]))

        return max(max(dp1),max(dp2))
                     
        
