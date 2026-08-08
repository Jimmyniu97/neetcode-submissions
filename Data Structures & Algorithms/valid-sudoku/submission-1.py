from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                curr = board[r][c]
                if curr == ".":
                    continue
                if curr in rows[r]:
                    return False
                if curr in cols[c]:
                    return False
                if curr in boxes[(r//3, c//3)]:
                    return False
                rows[r].add(curr)
                cols[c].add(curr)
                boxes[(r//3, c//3)].add(curr)
        
        return True