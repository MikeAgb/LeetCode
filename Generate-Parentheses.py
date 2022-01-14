class Solution:
    def generateParenthesis(self, n: int) -> List[str]: 
        result = []
        def backtrack(S=[], opened=0, closed=0): 
            if len(S) == 2*n:
                result.append("".join(S))
                return
            if opened<n:
                S.append("(")
                backtrack(S, opened+1, closed)
                S.pop()
                
            if(closed<opened):
                S.append(")")
                backtrack(S, opened, closed+1)
                S.pop()
        backtrack()
        return result
        
