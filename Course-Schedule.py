class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        
        courses = defaultdict(list)
        
        for pre in prerequisites:
            course, prereq = pre[0], pre[1]
            courses[prereq].append(course)
        
        visited = [False]*numCourses
        cycled = [False]*numCourses
        
        for course in range(numCourses):
            if(self.isCycle(course,courses,visited,cycled)):
                return False
        
        return True

    def isCycle(self,course,courses,visited,cycled):
        
        if(visited[course]):
            return False
        if(cycled[course]):
            return True
        
        cycled[course] = True
        seen_in_cycle = False
        for child in courses[course]:
            seen_in_cycle = self.isCycle(child,courses,visited,cycled)
            if(seen_in_cycle):
                break

        cycled[course] = False
        visited[course] = True
        return seen_in_cycle         
  
