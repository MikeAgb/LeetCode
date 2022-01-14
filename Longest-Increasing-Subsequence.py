class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = [nums[0]]
        for num in nums[1:]:
            if(num>sub[-1]):
                sub.append(num)
            else:
                i = 0
                while(num > sub[i]):
                    i+=1
                sub[i] = num
        return len(sub)
