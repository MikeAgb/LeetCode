from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = defaultdict(int)
     
        left = right = 0
        max_sub = 0
        
        while(right < len(s)):
            dic[s[right]]+=1
            # until we dont see a repeat
            while(dic[s[right]]>1):
               # print(right, left)
                dic[s[left]]-=1
                left+=1
            max_sub= max(max_sub, right-left+1)
            right+=1     
        return max_sub
                
                    
            
        
