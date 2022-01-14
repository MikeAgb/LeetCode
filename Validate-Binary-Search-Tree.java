/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    
    
    public boolean isValidBST(TreeNode root) {
        // in order traversal in array, check that array is ordered On
       // if(root==null){return true;}
      //  if(root.left!=null && root.left.val>=root.val){return false;}
      //  if(root.right!=null && root.right.val<=root.val){return false;}
        
        if(root==null){return true;}
        if(root.left!=null && getLargest(root.left, Integer.MIN_VALUE)>= root.val){return false;}
        if(root.right!=null && getSmallest(root.right,Integer.MAX_VALUE)<=root.val){return false;}
      //  System.out.println(getLargest(root,Integer.MIN_VALUE));
      //  System.out.println(getSmallest(root,Integer.MAX_VALUE));
        return isValidBST(root.left)&&isValidBST(root.right);
        
    }
    
    public int getLargest(TreeNode node, int max)
    {
        if(node==null){return max; }
        if(node.val>max){max = node.val;}
        int max2 = Math.max(getLargest(node.right, max),getLargest(node.left, max));
        return Math.max(max, max2);
    }
    
    public int getSmallest(TreeNode node, int min)
    {
        if(node==null){return min; }
        if(node.val<min){min = node.val;}
        int min2 = Math.min( getSmallest(node.left, min), getSmallest(node.right,min));
        return Math.min(min,min2);
    }
}
