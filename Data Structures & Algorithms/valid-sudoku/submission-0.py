class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, square = {i: set() for i in range(9)}, {i: set() for i in range(9)}, {i: set() for i in range(9)}
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                value = board[i][j]
                if value != ".":
                    if value not in row[i]:
                        row[i].add(value)
                    else:
                        return False
                    
                    if value not in col[j]:
                        col[j].add(value)
                    else:
                        return False
                    
                    if value not in square[(i//3)*3+(j//3)]:
                        square[(i//3)*3+(j//3)].add(value)
                    else:
                        return False
        
        return True