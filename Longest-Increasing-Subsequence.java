class Solution {
    
    public int lengthOfLIS(int[] nums) {
        if(nums.length==0){return 0;}
        int[] R = new int[nums.length];
        int answer = 1;
        
        for(int i = 0; i < nums.length;++i)
        {
            if(i==0){R[i] = 1;}
            
            else{int max = 1;
                for(int j = 0; j < i; ++j)
                {
                    if(nums[j]<nums[i]){ max = Math.max(max, R[j]+1);}
               
                }
                R[i] = max; 
                answer = Math.max(answer,max);          
            }  
        }
        return answer;     
        
    }
}
