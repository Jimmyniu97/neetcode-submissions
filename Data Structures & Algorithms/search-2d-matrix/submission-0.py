class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m-1
        while left <= right:
            mid = (left+right) // 2
            if matrix[mid][0] > target:
                right -= 1
            elif matrix[mid][0] < target:
                left += 1
            else:
                break
        row = (left+right) // 2
        left, right = 0, n-1
        while left <= right:
            mid = (left+right) // 2
            if matrix[row][mid] < target:
                left += 1
            elif matrix[row][mid] > target:
                right -= 1
            else:
                return True
        
        return False
        
