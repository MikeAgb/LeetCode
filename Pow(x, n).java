class Solution {
    public double helper(double x, int n) {
        if(n==0){return 1;}
        else if(x==1){return 1;}
        else
        {
            double half  = helper(x,n/2);
            if(n%2==0){
                
                return half*half;
            }
            else
            {
                return x*half*half;
            }
        }
    }    
    public double myPow(double x, int n)
    {
        int N = n;
        if(N<0)
        {
            N= -N;
            x = 1/x;
        }
        return helper(x,N);
    }
};
