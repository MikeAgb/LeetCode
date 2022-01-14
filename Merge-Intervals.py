class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals,key=lambda x:x[0])
        
        result = []
        
        prev_interval = intervals[0]
        prev_start, prev_end = prev_interval[0], prev_interval[1]
        
        for i in range(1,len(intervals)):
            interval = intervals[i]
            start, end = interval[0], interval[1]
            
            if(prev_end>=start):
                prev_start = min(start, prev_start)
                prev_end = max(end, prev_end)
            else:
                result.append([prev_start, prev_end])
                prev_start = start
                prev_end = end    
        result.append([prev_start, prev_end])
        return result
