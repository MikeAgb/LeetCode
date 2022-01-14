class Solution {
    public int maxArea(int[] height) {
        int maxVol = 0;
        
        int ptr1 = 0;
        int ptr2 = height.length-1;
        int smallerPtr;
        int a;
        int b;
        
        while(ptr1!=ptr2)
        {
            a = ptr2-ptr1;
            b = Math.min(height[ptr1],height[ptr2]);
            
            if(height[ptr1]<height[ptr2]){b = height[ptr1];}
            else{b = height[ptr2];}
            
            if((a*b)>maxVol){maxVol = a*b;}
            if(height[ptr2]>height[ptr1]){ptr1++;}
            else{ptr2--;}
        }
        return maxVol;
        
    }
}
