class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int start = 0;
        int end = matrix.length * matrix[0].length-1;
        int m = matrix.length;
        int n = matrix[0].length;
        int mid = (start+end)/2;
        
        while(start<=end)
        {
            int row = mid/n;
     
            int col = mid%n;
        
            if(matrix[row][col]<target)
            {
                // search right side
                start = mid+1;
                mid = (start+end)/2;
            }
            else if(matrix[row][col]>target)
            {
                end = mid-1;
                mid = (start+end)/2;
            }
            else
            {
                return true;
            }
        }    
        return false;

        
    }
}
