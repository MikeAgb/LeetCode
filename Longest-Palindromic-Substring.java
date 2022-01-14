class Solution {
    public String longestPalindrome(String s) {
        if(s==null){return null;}
        if(s.length()==1){return s;}
        
        int longest = 1;
        int start = 0;
        int end = 1;
        
        int [][] P = new int[s.length()][s.length()];
        
        for(int i = s.length()-1; i>=0; i--)
        {
            for(int j = i; j < s.length();j++)
            {
                if(i==j){P[i][j]=1;}
                else if(j-i==1 && s.charAt(i)==s.charAt(j) ){P[i][j]=1;}
                else if(P[i+1][j-1] ==1 && s.charAt(i)==s.charAt(j)) {P[i][j] =1;}
                if(P[i][j]==1)
                {
                    if(j-i+1>longest){
                        longest = j-i+1;
                        start = i;
                        end = j+1;
                    }
                }
              //  System.out.println(s.substring(i,j+1)+" "+P[i][j]);
               
            }
        }
     
        return s.substring(start,end);      
  
    } 
    
}
