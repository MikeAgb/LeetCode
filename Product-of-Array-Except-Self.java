class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] products = new int[nums.length];
        int[] L = new int[nums.length];
        int[] R = new int[nums.length];
        L[0] = 1;
        R[nums.length-1] = 1;
        for(int i = 1; i < nums.length; i++)
        {
            L[i] = L[i-1]*nums[i-1];
            R[nums.length-1-i] =R[nums.length-i]*nums[nums.length-i];
        }
        
        for(int i = 0; i < nums.length; i++)
        {
            products[i]  = L[i]*R[i];
        }     
        return products;     
    }
}
        
