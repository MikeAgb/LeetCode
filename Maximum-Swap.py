class Solution(object):
    def maximumSwap(self, num):
        
        str_num = str(num)
        max_num = num
        for i in range(0,len(str_num)-1):
            for j in range(i+1,len(str_num)):
              
                copy = list(str_num)
                temp = str_num[i]
                copy[i] = copy[j]
                copy[j] = temp
                current = int("".join(copy))
               
                if(current>max_num):
                    max_num = current
        return max_num              
