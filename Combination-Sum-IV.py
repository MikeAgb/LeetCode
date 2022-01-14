class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.helper(frozenset(nums), target)
      
    # memoization
    @lru_cache(maxsize=None)   
    # helper function recursive
    def helper(self,nums, current):
        nums_list = list(nums)
        if(current<=0): return 1
        result = 0
        for num in nums:
            if(current>=num):
                result+=self.helper(nums, current-num)
        return result
        
