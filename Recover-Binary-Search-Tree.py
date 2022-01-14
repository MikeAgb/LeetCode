# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ordered = self.inOrder(root) 
        first, second = self.find_swapped(ordered)
        self.helper_rec(root, ordered, first, second, 2)
 
    def helper_rec(self, root, ordered, first, second, number_swapped):
        if(root is None or number_swapped<=0):
            return
        else:
            if(root.val ==first or root.val==second):
                root.val = first if root.val == second else second
                number_swapped-=1
                if(number_swapped==0):
                    return
            
            self.helper_rec(root.left, ordered, first, second, number_swapped)
            self.helper_rec(root.right, ordered, first, second, number_swapped)
            
    def inOrder(self, node):
        if(node is None):
            return []
        return self.inOrder(node.left) + [node.val] + self.inOrder(node.right)
             
    def find_swapped(self, nums):
        first = second = math.inf
        for i in range(len(nums)-1):
            
            if(nums[i+1]< nums[i]):
                second = nums[i+1]
                if(first==math.inf):
                    first = nums[i]
                else:
                    break
        return first, second
