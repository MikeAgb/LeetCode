import numpy as np
class Solution:
    def maxA(self, n: int) -> int:
        # dynamic programming array
        arr = np.arange(n)+1
        for i in range(n):
            # pick where to start copy pasting if at all
            for j in range(i-3):
                # pick between only typing A's or starting the copy paste at j
                arr[i] = max(arr[i], arr[j]*(i-j-1))
        return arr[n-1]
            
