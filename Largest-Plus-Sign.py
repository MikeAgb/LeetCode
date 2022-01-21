import numpy as np
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
    
        grid = []
        
        for i in range(n):
            grid.append([1]*n)
            
        for mine in mines:
            grid[mine[0]][mine[1]] = 0
    
        arms =  []
        for i in range(n):
            arms.append([0]*n)
        
        for i in range(n):
            count = 0
            for j in range(n):
               
                # go right
                if(grid[i][j]==0):
                    count=0
                else:
                    count+=1
                arms[i][j] = count

            ## go left
            count = 0
            for j in range(n-1,-1,-1):
                
                if(grid[i][j]==0):
                    count=0
                else:
                    count+=1
                if(count< arms[i][j]): arms[i][j] = count

        for j in range(n):
            # go down
            count = 0
            for i in range(n):
                if(grid[i][j]==0):
                    count=0
                else:
                    count+=1
                if(count< arms[i][j]): arms[i][j] = count
            # go up
            count = 0
            for i in range(n-1,-1,-1):
                if(grid[i][j]==0):
                    count = 0
                else:
                    count+=1
                if(count< arms[i][j]): arms[i][j] = count

        return int(np.amax(arms))
       
