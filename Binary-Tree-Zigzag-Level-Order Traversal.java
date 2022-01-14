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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        boolean leftRight = false;
        Queue<TreeNode> q = new LinkedList<>();
        if(root==null){return new ArrayList<List<Integer>>();}
        int size = 0;
        int level = 1;
        List<List<Integer>> result = new ArrayList<>();
        q.add(root);
        q.add(null);
        List<Integer> currentLevel = new ArrayList<>();
        
        while(!q.isEmpty())
        {
            TreeNode current = q.poll();
            if(current!=null)
            {    
                currentLevel.add(current.val);
                if(current.left!=null){q.add(current.left);}
                if(current.right!=null){q.add(current.right);}
            }
            else{
          
                if(leftRight)
                {
                    Collections.reverse(currentLevel);
                    result.add(currentLevel);
                }
                else
                {
                    result.add(currentLevel);
                }
                leftRight=!leftRight;
                currentLevel = new ArrayList<Integer>();  
                if(q.size()>0)
                {
                q.add(null);
                }
            }
         
        }
        return result;

    }
}
