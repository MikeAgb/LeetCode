class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        from collections import defaultdict 
        dic = defaultdict(list)
        for word in strs:
            key = [0]*26
            for char in word:
                key[ord(char)-ord('a')]+=1
            dic[tuple(key)].append(word)
        return dic.values()
