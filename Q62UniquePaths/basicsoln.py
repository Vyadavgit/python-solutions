#  recursive approach exceeds time for bigger inputs
#  Time complexity: O(2^(m+n))
#  Space complexity: O(2^(m+n))
class Solution:
    def uniquePaths(self, m, n):
        return self.count(m,n)
    
    def count(self, m, n):
        if m == 1 or n == 1:
            return 1
        down = self.count(m-1, n)
        right = self.count(m, n-1)
        return down + right

solution_instance = Solution()
print(solution_instance.uniquePaths(3,7))
