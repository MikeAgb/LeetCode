/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head==null || head.next==null){return head;}
        ListNode ptr = head.next;
        ListNode lastDifferent = head;
        ListNode prev = null;
        boolean deleting = false;
        boolean allSame = true;
        while(ptr!=null)
        {
            System.out.println(ptr.val+" "+lastDifferent.val);
            if(ptr.val != lastDifferent.val)
            {
                allSame = false;
                if(deleting == false){
                 
                    ptr = ptr.next;
                    prev = lastDifferent;
                    lastDifferent = lastDifferent.next;
                }
                else
                {
                    deleting = false;
                    if(prev==null)
                    {
                        head = ptr;
                    }
                    else{ prev.next = ptr;}
                   
                    lastDifferent = ptr;
                    ptr = ptr.next;
             
                }
            }
            else{
                ptr = ptr.next;
                deleting = true;
            }
        }
        if(allSame){
            return null;}
        
        if(deleting)
        {
            if(prev!=null){prev.next = null;}
            else{return null;}
          
        }
        return head;    
    }
}
