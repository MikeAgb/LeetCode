from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
            

class Trie:
   
    def __init__(self):
        
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        
        current = self.root
        for c in word:
            current = current.children[c]
        current.isWord = True
        

    def search(self, word: str) -> bool:
        
        current = self.root
        for c in word:
            current = current.children.get(c)
            if not current:
                return False
        return current.isWord
                

    def startsWith(self, prefix: str) -> bool:
        
        current = self.root
        for c in prefix:
            current = current.children.get(c)
            if not current:
                return False
        return True
       
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
