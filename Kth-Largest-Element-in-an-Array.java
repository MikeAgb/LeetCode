class Solution {

    public int findKthLargest(int[] nums, int k) {

        Queue<Integer> q = new PriorityQueue<>();
        for(int i = 0; i < nums.length; ++i)
        {
            if(q.size() <k)
            {
                q.add(nums[i]);
            }
            else if(nums[i]>q.peek())
            {
                q.remove();
                q.add(nums[i]);
            }
        }
        return q.peek(); 
    }
}
