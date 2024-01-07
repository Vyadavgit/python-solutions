
# Q54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#         Output: [1,2,3,6,9,8,7,4,5]
# Time Complexity: O(m * n) , where m = rows, n = cols
# Space Complexity: O(m + n) , where m = rows, n = cols

class Solution:
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     return self.traverse(matrix, 0, 0, [])
    def spiralOrder(self):
        matrix = [[1,2,3], [4, 5, 6], [7,8,9]]
        print(self.traverse(matrix, 0, 0, []))

        matrix = [[1]]
        print(self.traverse(matrix, 0, 0, []))

        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        print(self.traverse(matrix, 0, 0, []))
        
    
    def traverse(self, arr, i, j, res):
        if arr[i][j] != float('-inf'): # -ve infinity
            res.append(arr[i][j])
            arr[i][j] = float('-inf')
        
        if j < len(arr[i])-1 and arr[i][j+1] != float('-inf'): # traverse right
            self.traverse(arr, i, j+1, res)
        elif i < len(arr)-1 and arr[i+1][j] != float('-inf'): # traverse down
            self.traverse(arr, i+1, j, res)
        elif j > 0 and arr[i][j-1] != float('-inf'): # traverse left
            self.traverse(arr, i, j-1, res)
        
        if i > 0 and arr[i-1][j] != float('-inf'): # traverse upwards
            while arr[i-1][j] != float('-inf'):
                i -= 1
                res.append(arr[i][j])
                arr[i][j] = float('-inf')
            self.traverse(arr, i, j+1, res) # traverse right again
        return res
    
# create an instance 
solution_instance = Solution()

# call method
solution_instance.spiralOrder()

