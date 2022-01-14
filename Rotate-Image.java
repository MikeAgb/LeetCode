class Solution {
    public void rotate(int[][] matrix) {
        
        int layers = (int)Math.ceil((float)matrix.length/2);
        int n = matrix.length-1;
        for(int layer = 0; layer < layers; layer++)
        { 
            for(int i =0; i < n-2*layer; i++)
            {
                System.out.println(layer+" "+i);
                int top = matrix[layer][i+layer];
                int right = matrix[i+layer][n-layer];    
                int left = matrix[n-layer-i][layer];
                int bot =matrix[n-layer][n-layer-i] ;

                //top -> right
                matrix[i+layer][n-layer] = top;
                
                // right -> bot
                matrix[n-layer][n-layer-i]= right;
                
                //bot -> left
                
                matrix[n-layer-i][layer] = bot;
                
                //left-> to
                matrix[layer][i+layer] = left;
                
            }
        }
        
    }
}
