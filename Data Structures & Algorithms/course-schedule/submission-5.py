class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        courses = dict({i:[] for i in range(numCourses)})

        for a, b in prerequisites:
            courses[a].append(b)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if courses[crs] == []:
                return True
            visited.add(crs)
            for pre in courses[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            courses[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True
