# 79. Word Search

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input board:
#     A B C E
#     S F C S 
#     A D E E 

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# DFS and Back tracking technique
# TIME AND SPACE COMPLEXITY
# The time complexity of the exist method is O(M * N * 4^L), where M is the number of rows in the board, N is the number of columns in the board, and L is the length of the word.
# Space completely is O(M * N)

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(board, word, i, j, idx, visited):
            if idx == len(word): return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word[idx] or visited[i][j]: return False
            visited[i][j] = True
            # dfs
            if (search(board, word, i+1, j, idx+1, visited) # down
            or search(board, word, i, j+1, idx+1, visited)  # right
            or search(board, word, i-1, j, idx+1, visited)  # up
            or search(board, word, i, j-1, idx+1, visited)): # left
                return True
            visited[i][j] = False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and search(board, word, i, j, 0, [[False]*len(board[0]) for _ in range(len(board))]):
                    return True
        return False
    
solution_instance = Solution()
print(solution_instance.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))

    
