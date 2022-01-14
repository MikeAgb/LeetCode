class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        List<List<Integer>> list = new ArrayList();
        
        Arrays.sort(nums);
        
        int i = 0;
        int lo = 0;
        int hi = 0;
        
        while(i < nums.length && nums[i]<=0)
        {
            if(i==0 || nums[i]!=nums[i-1]){
                lo = i+1;
                hi = nums.length-1;
                while(lo<hi)
                {
               
                    if(nums[lo]+nums[hi]+nums[i] == 0)
                    {
                        ArrayList<Integer> current = new ArrayList<>();
                        current.add(nums[i]);
                        current.add(nums[lo]);
                        current.add(nums[hi]);
                        list.add(current);
                        lo++;
                        hi--;
                        while (lo < hi && nums[lo] == nums[lo - 1])
                            ++lo;
                    
                    }
                    else if(nums[lo]+nums[hi]+nums[i] < 0){lo++;}
                    else{hi--;}
                }
            }
            i++;
        }   
        return list;
    }
}
