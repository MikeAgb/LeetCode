# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode],arr=[]):     
        self.arr = []
        self.inOrder( self.arr, root)
        print(self.arr)
        self.ptr = -1
        
    def inOrder(self,arr,root):  
        if(root==None): return
        self.inOrder(arr,root.left)
        arr.append(root.val)
        self.inOrder(arr,root.right)
        
    def next(self) -> int:
  
        self.ptr+=1
        return self.arr[self.ptr]  

    def hasNext(self) -> bool:
        if(self.ptr < len(self.arr)-1):
            return True
        return False
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
