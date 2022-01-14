class Solution {
    public int kthSmallest(int[][] matrix, int k) {
      
      // use priorityQueue as min heap to store the items
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
      // fill the heap
        for(int i = 0; i < matrix.length; ++i)
        {
            for(int j = 0; j < matrix.length; ++j)
            {
                minHeap.add(matrix[i][j]);
            }
        }
        int pop = 0;
      // pop the k elements from the heap
        for(int i = 0; i < k; i++)
        {
            pop = minHeap.remove();
        }
        return pop;
    }
}
