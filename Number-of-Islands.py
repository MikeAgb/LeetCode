class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
        
                if(grid[i][j]=="1"):
                    
                    count+=1
                    self.helperDFS(grid,i,j)
        return count

    def helperDFS(self, grid,i,j):
        
        if(i<0 or j <0 or i >= len(grid) or j >= len(grid[0])): return 
        
        if(grid[i][j]=="0"): return
        if(grid[i][j]=="1"):
            grid[i][j]="0"
            
            self.helperDFS(grid,i+1,j)
            self.helperDFS(grid,i-1,j)
            self.helperDFS(grid,i,j+1)
            self.helperDFS(grid,i,j-1)
        
        
        
