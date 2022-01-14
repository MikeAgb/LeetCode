from collections import defaultdict
from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a graph is a tree iff it is fully connected and has no cycles
        # construct graph as a adjacency list
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        seen = set()
        seen.add(0)
        stack = deque()
        stack.append(0)
        
        while(stack):
            node = stack.pop()
            for neighbour in graph[node]:
              # cycle
                if(neighbour in seen):
                    return False
                else:
                    stack.append(neighbour)
                    seen.add(neighbour)
                    graph[neighbour].remove(node)    
        # fully connected
        return len(seen) == n
    
     
