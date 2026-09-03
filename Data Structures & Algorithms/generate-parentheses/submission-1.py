class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(curr, l, r):
            if r > l:
                return
            if len(curr) == 2*n:
                if l == r:
                    res.append(curr)
                return
            
            dfs(curr + "(", l+1, r)
            dfs(curr + ")", l, r+1)
        
        dfs("", 0, 0)
        return res