class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(i, j, suffix, board):
        # we are done
            if len(suffix) == 0:
                return True
        
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j]!=suffix[0]:
                return False
        
            # so it cannot be reused
            board[i][j] = '#'
        
            for x,y in [(0,1), (-1,0), (0,-1),(1,0)]:
            
                if helper(i+x, j+y, suffix[1:], board):
             
                    return True
            
            board[i][j] = suffix[0]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i,j, word, board):
                    return True
        return False
    
