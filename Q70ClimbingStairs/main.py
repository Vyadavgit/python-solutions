# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps


# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)

        def paths(n, memo):
            if n <= 1: return 1
            if memo[n] != 0:
                return memo[n]
            memo[n] = paths(n-1, memo) + paths(n-2, memo)
            return memo[n]
    
        return paths(n, memo)
    

        
solution_instance = Solution()
print(solution_instance.climbStairs(5))