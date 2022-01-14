# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.helper(root, math.inf, -math.inf)
    
    def helper(self,root, max_val, min_val): 
        if(not root): return True
        if(root.val >= max_val or root.val <= min_val): return False
        return self.helper(root.left, root.val, min_val) and self.helper(root.right, max_val, root.val)
    
    
