class Solution {
    public int[] searchRange(int[] nums, int target) {
        
        int start = 0;
        int end = nums.length-1;
        int mid = (end+start)/2;
        boolean found = false;
        while(start<=end)
        {
            int key = nums[mid];
            
            if(key == target)
            {
                found = true;
                start = end+1;
            }
            else if( key < target)
            {
                start = mid+1;
                mid = (end+start)/2;
            }
            else{
                end = mid-1;
                mid = (end+start)/2;
                
            }
        }
        
        if(!found){
            int[] result = {-1,-1};
            return result;
        }
        
        int first = mid;
        int last = mid;
        while(first>=0 && nums[first] == target)
        {
            first--;
        }
        while(last < nums.length && nums[last] == target)
        {
            last++;
        }
        int [] result =  {first+1, last-1};
        return  result;
    }
}
