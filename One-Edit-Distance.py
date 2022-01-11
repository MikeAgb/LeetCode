class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # if their lengths differ by more than one they cannot be one edit apart
        if abs(len(s)-len(t))>1 or s == t:
            return False
        else:
            # edit counter
            diff_count = 0
            # assume len(s) > len(t) otherwise swap them
            if len(s) < len(t):
                return self.isOneEditDistance(t,s)
            else:
                # 2 pointer approach
                ptr1 = ptr2 = 0
                while ptr1 < len(s) and ptr2 < len(t):
                    # if there is a difference
                    if s[ptr1] != t[ptr2]:
                        # increment difference counter
                        diff_count+=1 
                        # if they have the same lenght, move bioth pointers
                        if len(s) == len(t):
                            ptr1+=1
                            ptr2+=1
                        # otherwise, don't move the pointer for the shorter string
                        else:
                            ptr1+=1
                    else:
                        ptr1+=1
                        ptr2+=1
                    if diff_count > 1:
                        return False
            return True
