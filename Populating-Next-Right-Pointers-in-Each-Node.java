/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        
        if(root==null){return null;}
        
        Queue<Node> q = new ArrayDeque<>();
        q.add(root);
        int level = 0;
        int count = 0;
        boolean previousVisited = true;
        Node previous = null;
        while(!q.isEmpty())
        {
            Node current = q.remove();
            count++;
            if(count>Math.pow(2,level+1)-1){level++;}
            
            if(count==Math.pow(2,level+1)-1){
                if(previous!=null){previous.next = current;}
                current.next= null;
            }
            System.out.println(count+ " "+level);
            if(count!=Math.pow(2,level))
            {
                previous.next=current;
            }
            
              previous = current; 
             if(current.left!=null && current.right!=null)
            {
                q.add(current.left) ;
                q.add(current.right);
            }
                
            }
           
        return root;
        }
        
     
}
