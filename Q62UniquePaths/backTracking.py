# 62. Unique Paths
#         There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

#         Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

#         The test cases are generated so that the answer will be less than or equal to 2 * 109.

#  backTracking approach
#  Time complexity: O(mxn)
#  Space complexity: O(mxn)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {} # memorization dict
        
        def backTrack(x, y):
            if x == m-1 and y == n-1: return 1 # reached destination so return it

            if (x, y) in memo:
                return memo[(x,y)]
            
            down = 0 if x == m-1 else backTrack(x+1, y)
            right = 0 if y == n-1 else backTrack(x, y+1)

            memo[(x,y)] = down + right

            return memo[(x,y)]
        return backTrack(0,0)

solution_instance = Solution()
print(solution_instance.uniquePaths(3,7))










