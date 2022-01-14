# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        x = []
        self.inOrder(root,x,k)
        return x[-1]
    
    def inOrder(self, root, arr,k):
        
        if(not root):
            return arr
        else:
            if(len(arr)>=k):
                return arr
            self.inOrder(root.left, arr,k)
            
            if(len(arr)>=k):
                return arr
            
            arr.append(root.val)
            
            if(len(arr)>=k):
                return arr
            
            self.inOrder(root.right,arr,k)
        
