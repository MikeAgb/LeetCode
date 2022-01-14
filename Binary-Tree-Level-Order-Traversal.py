# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        result = []
        if not root:
            return result
        q.append(root)
        node = 0
        current_row = []
        while(q):    
            current_len = len(q)
            current_row = []
            for i in range(current_len):    
                current = q.pop()
                if(current):
                    current_row.append(current.val)
                if(current.left):
                    q.insert(0,current.left)
                if(current.right):
                    q.insert(0, current.right)
            result.append(current_row)
                
        return result
