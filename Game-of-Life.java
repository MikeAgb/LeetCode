class Solution {
    public void gameOfLife(int[][] board) {
        if(board.length==0){return;}
        int[][] newBoard = new int[board.length][board[0].length];
            for(int i = 0; i < board.length; i++)
            {
                for(int j = 0; j < board[0].length; j++){
                   
                    int top;
                    int right;
                    int left;
                    int bot;
                    int rightBot;
                    int leftBot;
                    int rightTop;
                    int leftTop;
                    
                    if(i>0){top = board[i-1][j];}
                    else{top  = 0 ;}
                    
                    if(j < board[0].length-1){right = board[i][j+1];}
                    else{right = 0;}
                    
                    if(j>0){left = board[i][j-1];}
                    else{left = 0;}
                    
                    if(i<board.length-1){bot = board[i+1][j];}
                    else{bot = 0;}
                    
                    if(j==(board[0].length-1) || i==(board.length-1)){rightBot=0;}
                    else{rightBot = board[i+1][j+1];}
                    
                    if(j==0 || i == board.length-1){leftBot=0;}
                    else{leftBot = board[i+1][j-1];}
                    
                    if(i==0 || j== board[0].length-1){rightTop=0;}
                    else{rightTop = board[i-1][j+1];}
                    
                    if(i==0 || j==0){leftTop=0;}
                    else{leftTop = board[i-1][j-1];}
                    
                    int num_live = top+bot+left+right+leftBot+rightBot+leftTop+rightTop;
                    
                    if(board[i][j]==1)
                    {
                        if(num_live<2 || num_live>=4){newBoard[i][j]=0;}
                        else {newBoard[i][j] = 1;}
                    }
                    
                    else
                    {
                        if(num_live==3){newBoard[i][j]=1;}
                        else{newBoard[i][j] = 0;}
                    }         
                    System.out.println(num_live);
          
                }
            }
         for(int i = 0; i < board.length;i++)
        {
            for(int j = 0; j < board[0].length;j++)
            {
                board[i][j] = newBoard[i][j];
            }
        }
       
    }
}
