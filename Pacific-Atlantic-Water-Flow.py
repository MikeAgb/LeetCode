class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if(not heights or not heights[0]):
            return []
        
        pacific = set()
        atlantic = set()
        
        m = len(heights)
        n = len(heights[0])

        for i in range(m):
            self.dfs(i,0,pacific, m,n, heights)
            self.dfs(i,n-1, atlantic, m,n, heights)
         
        for j in range(n):
            self.dfs(0,j, pacific,m,n,heights)
            self.dfs(m-1,j, atlantic,m,n, heights)
            
        return list(pacific.intersection(atlantic))
 
# depth first search recursive
    def dfs(self, i,j, ocean, m,n, heights):
        # reached from ocean
        ocean.add((i,j))
        
        for (x,y) in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_i = i+x
            new_j = j+y
            
            if(new_i<0 or new_j < 0 or new_i >=m or new_j >= n):
                continue
            if (new_i, new_j) in ocean:
                continue
            if(heights[new_i][new_j] < heights[i][j]):
                continue
            else:
                self.dfs(new_i, new_j, ocean, m,n, heights)
            
        
