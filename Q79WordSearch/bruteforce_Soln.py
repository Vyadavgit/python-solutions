# 79. Word Search

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# Example 1:
# Input board:
#     A B C E
#     S F C S 
#     A D E E 

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# TIMR AND SPACE COMPLEXITY:
# The time complexity of the exist function in the provided code is O(M * N * 4^L), where M is the number of rows in the board, N is the number of columns in the board, and L is the length of the word. This is because for each cell in the board, the function performs a recursive search in four directions (up, down, left, right) for a maximum depth of L (length of the word). Since each recursive call explores four possible directions, the total number of recursive calls is 4^L. Therefore, the overall time complexity is O(M * N * 4^L).

# The space complexity of the exist function is O(L), where L is the length of the word. This is because the function uses a boolean matrix visited of size M * N to keep track of visited cells, which requires O(M * N) space. Additionally, the function uses a string newString to store the current path being explored, which can have a maximum length of L. Therefore, the overall space complexity is O(L).

# this solution is not an optimized approach as it explores all paths

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    def recursion(board, word, r, c, newStr, found, visited):
        if (r >= 0 and r < len(board)) and (c >= 0 and c < len(board[0])) and not(found):
            newStr = newStr + board[r][c]
            visited[r][c] = True

            if len(newStr) == len(word) and newStr == word:
                return True
            elif len(newStr) >= len(word):
                return found
            else:
                if c < len(board[0])-1 and not(visited[r][c+1]):
                    found = found or recursion(board, word, r, c+1, newStr, found, visited) # right
                    visited[r][c+1] = False
                if c > 0 and not(visited[r][c-1]):
                    found = found or recursion(board, word, r, c-1, newStr, found, visited) # left
                    visited[r][c-1] = False
                if r < len(board)-1 and not(visited[r+1][c]):
                    found = found or recursion(board, word, r+1, c, newStr, found, visited) # Down
                    visited[r+1][c] = False
                if r > 0 and not(visited[r-1][c]):
                    found = found or recursion(board, word, r-1, c, newStr, found, visited) # Up
                    visited[r-1][c] = False
            visited[r][c] = False
        return found 

    ispresent = False
    for r in range(len(board)):
        for c in range(len(board[0])):
            ispresent = ispresent or recursion(board, word, r, c, "", False, [[False] * len(board[0]) for _ in range(len(board))])
            if ispresent: return True
    return ispresent

def main():
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    print(exist(board, "SEE"))

if __name__ == "__main__":
    main()

