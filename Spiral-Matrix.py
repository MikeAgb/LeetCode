class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = []
        layers = math.ceil(min(m,n)/2)
        
        for layer in range(layers):
            i = j = layer

            hori = n-2*layer
            verti = m-2*layer
            
            size = hori*verti -max((hori-2),0)*max((verti-2),0)
            for step in range(size):
                result.append(matrix[i][j])
                #moving right
                if(step<hori-1):
                    j+=1
                 
                    continue
                if(step>= hori-1 and step <hori-2+verti):
                    i+=1
                  
                    continue
                if(step>= hori-2+verti and step < hori-3+verti+hori ):
                    j-=1
                   
                    continue
                else:
                    i-=1    
        return result
