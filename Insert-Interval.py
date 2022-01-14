class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        start = newInterval[0]
        end = newInterval[1]
        result = []
        i = 0
        ## add all interval starting before nmew one
        while(i < len(intervals) and start > intervals[i][0]):
            result.append(intervals[i])
            i+=1
        ## add new one and merge its to last if needed
        if(not result or result[-1][1]<start):
            result.append(newInterval)
        else:
            result[-1][1] = max(result[-1][1], end)
        
        
        while(i < len(intervals)):
            
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            
            if(result[-1][1] < current_start):
                result.append(intervals[i])
            else:
                result[-1][1] = max(current_end, result[-1][1])
            i+=1
        return result    
