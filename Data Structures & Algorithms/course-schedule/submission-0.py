class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        path = set()

        def dfs(course):
            if course in path:
                return False
            
            path.add(course)
            
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            path.remove(course)
            
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


