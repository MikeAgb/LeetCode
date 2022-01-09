class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # base condition
        if len(s)==0:
            return 0
        count = 0
        for c in s:   
            if s.count(c)<k:
                return max(self.longestSubstring(s[:count],k),self.longestSubstring(s[count+1:],k))
            count+=1
        return len(s)
