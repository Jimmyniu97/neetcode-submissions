class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        current = []
        def dfs(open, close):
            if close > open or open > n:
                return
            elif len(current) == 2*n:
                res.append("".join(current.copy()))
                return
            
            current.append("(")
            dfs(open+1, close)
            current.pop()

            current.append(")")
            dfs(open, close+1)
            current.pop()
        
        dfs(0,0)
        return res
