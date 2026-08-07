class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = set()
        visited = set()
        ans = []
        graph = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        def dfs(course):
            if course in path:
                return False
            path.add(course)
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            path.remove(course)
            if course not in visited:
                visited.add(course)
                ans.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return ans
            