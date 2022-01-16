class Solution {
    public int maximumSwap(int num) {
        //java implementation with arraylist
        String str_num = ""+num;
        ArrayList<Integer> list_num = new ArrayList();
    
        int first_index = 0;
        boolean foundFirst = false;
        int largest = 0;
        for(int i = 0; i < str_num.length(); i++)
        {
            list_num.add(Character.getNumericValue(str_num.charAt(i)));
            if(i!=0)
            {
                if(Integer.parseInt(""+str_num.charAt(i)) > Integer.parseInt(""+str_num.charAt(i-1)) && !foundFirst)
                {
                    foundFirst = true;
                    
                }
                
                if(foundFirst && Character.getNumericValue(str_num.charAt(i))>=largest)
                {
                    largest = Character.getNumericValue(str_num.charAt(i));
                    first_index = i;
                }
            }
            
        }
        
        int num_at_first = Integer.parseInt(""+str_num.charAt(first_index));
        
        for(int i = 0; i < first_index; i++)
        {
            if(Integer.parseInt(""+str_num.charAt(i))< num_at_first)
            {
                int temp = list_num.get(i);
                list_num.set(i,num_at_first);
                list_num.set(first_index,temp);
                
                StringBuilder s = new StringBuilder();
                for(int j= 0; j < list_num.size();j++)
                {
                    s.append(list_num.get(j));
                    
                }
                return Integer.parseInt(s.toString());
                
            }
        }
        
        return num;
        
    }
}
