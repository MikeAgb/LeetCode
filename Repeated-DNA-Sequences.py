class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # hashset
        sequences = set()
        repeated = []
        # iterate over sequence
        for i in range(len(s)-9):
            # extract subsequence
            sequence = s[i:i+10]
            # if already seen, add to result
            if sequence in sequences:
                repeated.append(sequence)
            sequences.add(sequence)
        # remove duplicates
        return list(set(repeated))
                
