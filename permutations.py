class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(x):
          ### if at end of sequence, append copy to solutions
            if x == len(nums):
                output.append(nums[:])
            ## else for each digit after this one, swap it with this one and call on next number
            for i in range(x,len(nums)):
                nums[x], nums[i] = nums[i], nums[x]
                helper(x+1)
                # swap them back
                nums[x], nums[i] = nums[i], nums[x]
                
        output = []
        helper(0)
        return output
