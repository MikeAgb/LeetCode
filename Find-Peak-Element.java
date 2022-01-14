class Solution {
    public int findPeakElement(int[] nums) {
        
        int start = 0;
        int end = nums.length-1;
        int mid = (start+end)/2;
        if(nums.length==1){return 0;}
        while(start<=end)
        {
            if(start == end){return start;}
           if(nums[mid] > nums[mid+1])
           {
               end = mid;
                mid = (start+end)/2;
           } 
            else
            {
                start = mid+1;
                mid = (start+end)/2;
            }
        }     
        return start;
    }
}
