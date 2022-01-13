class Solution(object):
    def setZeroes(self, matrix):
   
        first_row = False
        first_col = False
        
        M = len(matrix)
        N = len(matrix[0])
        for i in range(M):
            if(matrix[i][0]==0):
                first_col = True
        
        for i in range(N):
            if(matrix[0][i]==0):
                first_row = True
        
        for i in range(len(matrix)):
          
            for j in range(len(matrix[0])):
                
                if(matrix[i][j] == 0):
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if(matrix[i][0] == 0): 
                    matrix[i][j] = 0
                if(matrix[0][j] == 0):
                    matrix[i][j] = 0   
        print(first_row, first_col)     
        if(first_col):
            for i in range(M):
                print("here")
                matrix[i][0] = 0
                
        if(first_row):
            for i in range(N):
                matrix[0][i] = 0
                    
       
      
      
                
        
      
        
