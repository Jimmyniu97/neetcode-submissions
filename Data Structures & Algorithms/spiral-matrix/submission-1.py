class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        moves = [[0,1],[1,0],[0,-1],[-1,0]]
        choice = 0
        i, j = 0, 0
        visited = {(i,j)}
        res = [matrix[i][j]]
        
        while len(res) != m * n:
            x,y = moves[choice][0], moves[choice][1]
            row, col = i + x, j + y
            if 0 <= row < m and 0 <= col < n and (row, col) not in visited:
                visited.add((row, col))
                res.append(matrix[row][col])
                i, j = row, col
            else:
                choice = (choice+1) % len(moves)
            
        
        return res