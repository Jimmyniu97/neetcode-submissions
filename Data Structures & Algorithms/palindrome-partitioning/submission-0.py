class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def isPalindrome(i, j):
            while j < i:
                if s[j] == s[i]:
                    j += 1
                    i -= 1
                else:
                    return False
            return True

        def dfs(i, j):
            if j >= len(s):
                res.append(path.copy())
                return
            
            if i >= len(s):
                return
            
            dfs(i+1, j)
            if isPalindrome(i,j):
                path.append(s[j:i+1])
                dfs(i+1, i+1)
                path.pop()
        
        dfs(0, 0)
        return res