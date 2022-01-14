class RandomizedSet {
    ArrayList<Integer> list = new ArrayList<>();
    HashMap<Integer,Integer> map = new HashMap<>();
    /** Initialize your data structure here. */
    public RandomizedSet() {

    }    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if(map.containsKey(val)){return false;}
        else
        {
            map.put(val, list.size());
            list.add(val);
            return true;
        }
    }
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        
        if(map.containsKey(val) && list.size()>1)
        {
            int index = map.get(val);
            map.remove(val);
            int last = list.get(list.size()-1);
            list.set(index,last);
            if(last!=val){map.put(last,index);}
          
            list.remove(list.size()-1);
           
            return true;
        }
        else if (map.containsKey(val) && list.size()==1)
        {
            map.remove(val);
            list.remove(0);
            
            return true;
        }
        else{return false;}
        
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
   
        Random ran = new Random();
        int x = ran.nextInt(list.size());
        return list.get(x);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
