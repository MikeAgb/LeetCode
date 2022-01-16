import numpy as np
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        right = len(s)//2
        left = right+1
        result = 0
        
        # dynamic programing solution
        dp = np.zeros((len(s),len(s)))
        
        for i in range(len(s)):
            dp[i][i] = 1
            
        for i in range(len(s)-1):
            if(s[i]==s[i+1]):
                dp[i][i+1] = True
            result+= dp[i][i+1]

        for l in range(3,len(s)+1):
            i=0
            j=i+l-1
            while(j<len(s)):
                if(dp[i+1][j-1]==1 and s[i] == s[j]):
                    dp[i][j] = 1
                    result+=1
                i+=1
                j+=1
        
        return int(result+len(s))
    
   
        
