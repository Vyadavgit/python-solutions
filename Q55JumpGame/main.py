# 55. Jump Game
# You are given an integer array nums. You are initially positioned at the array's first index,
#  and each element in the array represents your maximum jump length at that position.
#  Return true if you can reach the last index, or false otherwise.
#         Example 1:
#         Input: nums = [2,3,1,1,4]
#         Output: true
#         Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

#  Time complexity: O(N)
#  Space complexity: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxPos = 0
        for i in range(len(nums)):
            if i > maxPos:
                return False
            maxPos = max(maxPos, i + nums[i])
            if maxPos >= len(nums)-1:
                return True
        return False
