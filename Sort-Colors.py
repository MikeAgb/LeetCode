class Solution:
   
    def quickSort( self,nums,lo, hi):
        
        if lo< hi:
            index = self.find_pivot(nums, lo, hi)
            
            self.quickSort(nums, index+1, hi)
            self.quickSort(nums, lo, index-1)
            
    
    def find_pivot(self,nums, lo, hi):
        
        pivot = nums[hi]
        index = lo-1
        for j in range(lo, hi):
            
            if(nums[j]< pivot):
                index+=1
                temp = nums[index]
                nums[index] = nums[j]
                nums[j] = temp
        temp =  nums[index+1]  
        nums[index+1] = nums[hi]
        nums[hi]  = temp
        
        return index+1
        
    def sortColors(self, nums: List[int]) -> None:
        
        self.quickSort(nums,0, len(nums)-1)
     
        
