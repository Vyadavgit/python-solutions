# 73. Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# time complexity: O(r*c)
# space complexity: O(r+c)

class Solution:
    def setZeros(self, matrix: List[List[int]]) -> None:
        setRows = [False]*len(matrix)
        setColumns = [False]*len(matrix[0])

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    setRows[r] = True
                    setColumns[c] = True
        
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if setRows[r] or setColumns[c]:
                    matrix[r][c] = 0
