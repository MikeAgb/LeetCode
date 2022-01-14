class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ## check if its 9x9
        # each row:
        for r in range(9):
            seen = [0]*9
            for c in range(9):
              
                value = board[r][c]
                if(value != '.'):
                    value = int(value)-1
                    if(seen[value] == 1):
                        return False
                    else:
                        seen[value] = 1
        # each column
        for c in range(9):
            seen = [0]*9
            for r in range(9):
                value = board[r][c]
                if(value != '.'):
                    value = int(value)-1
                    if(seen[value] == 1):
                        return False
                    else:
                        seen[value] = 1
        # for each box:
        for i in range(3):
            for j in range(3):
                seen = [0]*9
                for r in range(3*i,3*i+3):
                    for c in range(3*j,3*j+3):
                      #  print(r,c)
                        value = board[r][c]
                        if(value != '.'):
                            value = int(value)-1
                            if(seen[value] == 1):
                                return False
                            else:
                                seen[value] = 1
        return True
                
