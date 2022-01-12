class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_kills = 0
        # iterate over grid
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    max_kills = max(max_kills, self.helper(grid,i,j))
        return max_kills
    
    def helper(self,grid,x,y):
        kills = 0
        # current row
        for i in range(x, len(grid)):
            if grid[i][y] == 'E':
                kills+=1
            elif grid[i][y] == 'W':
                break
        for i in range(x-1,-1,-1):
            if grid[i][y] == 'E':
                kills+=1
            elif grid[i][y] == 'W':
                break
        # current column
        for j in range(y,len(grid[0])):
            if grid[x][j] == 'E':
                kills+=1
            elif grid[x][j] == 'W':
                break
        for j in range(y-1,-1,-1):
            if grid[x][j] == 'E':
                kills+=1
            elif grid[x][j] == 'W':
                break
        return kills
       
        
