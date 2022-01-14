class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(int i= 0; i < nums.length; i++){
            
            if(!map.containsKey(nums[i]))
            {
                map.put(nums[i],1);
            }
            else{
                map.put(nums[i], map.get(nums[i])+1);
            }
        }
        
        Queue<Integer> heap = new PriorityQueue<>(
        (n1,n2) -> map.get(n1) - map.get(n2)
        );
        
        for(int key: map.keySet())
        {
            heap.add(key);
            if(heap.size()>k)
            {
                heap.poll();
            }
        }
        
        int[] frequents = new int[k];
        
        for(int i = 0; i < k; i++)
        {
            frequents[i] = heap.poll();
        }
        return frequents;
        
    }
}
