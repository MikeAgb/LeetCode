class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # sort by start time of intervals
        slots1.sort()
        slots2.sort()
        ptr1 = ptr2 = 0
        # 2 pointer method
        while ptr1 < len(slots1) and ptr2 < len(slots2):
            # find the overlap and check if it is larger than the duration
            left = max(slots1[ptr1][0],slots2[ptr2][0])
            right = min(slots1[ptr1][1],slots2[ptr2][1])
            if right - left >= duration:
                earliest = [left,left+duration]
                return earliest
            # advance the pointer of the interval which ends first
            elif slots1[ptr1][1] > slots2[ptr2][1]:
                ptr2+=1
            else:
                ptr1+=1
        # otherwise return empty array
        return []
        
        
            
        
        
