class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # dynamic programming solution
        left = 0
        freq = [0]*26
        max_ = 0
        mostFreq = 0
        
        for right in range(len(s)):
            
            freq[ord(s[right])-ord('A')]+=1
            mostFreq = max(freq)
            lettersToChange = right-left+1 - mostFreq
            if(lettersToChange>k):
                freq[ord(s[left])-ord('A')]-=1
                left+=1
            max_ = max(max_,right-left+1)

        return max_
        
