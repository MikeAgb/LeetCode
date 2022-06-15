class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        solution =[[]]
        # for each number in the list, add it to each set in so far
        for num in nums:
            solution += [current + [num] for current in solution]
        return solution
