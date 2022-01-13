class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        spiral = [[0 for x in range(n)] for y in range(n)]
        
        current = 0
        
        layers = int(math.ceil(n/2))
    
        for layer in range(layers+1):
            
            size = n-2*layer-1
            if(size==0):      
                spiral[layer][layer] = current+1
            for i in range(4*(size)):
                ### top
                current+=1
                if (i <size):
                    spiral[layer][i%size+layer] = current
                ### right side
                elif( i>=size and i < 2*size):
                    spiral[i%size+layer][size+layer] =current
                ## bottom
                elif( i>= 2*size and i < 3*size):
                    spiral[size+layer][size-i%size+layer] = current
                ### left
                else:
                    spiral[size+layer-i%size][layer] = current
            
        return spiral
                    
                
                
        
