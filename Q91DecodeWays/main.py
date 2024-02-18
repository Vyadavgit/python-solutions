# Q91. Decode Ways
# A message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"

# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

# TIME AND SPACE COMPLEXITY
# The time complexity of the numDecodings method in the given code is O(n), where n is the length of the input string s. This is because the method uses recursion to explore all possible decodings, and for each recursive call, it reduces the size of the input string by 1 or 2 characters.
# The space complexity of the numDecodings method is O(n), where n is the length of the input string s. This is because the method uses a memoization dictionary memo to store the results of subproblems, and the size of the dictionary can grow up to the length of the input string. Additionally, the recursion stack also contributes to the space complexity, but it is limited to the maximum depth of recursion, which is also proportional to the length of the input string.
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        memo = {}
        
        def recursion(s):
            if not s:  # Add a check to ensure that the string is not empty
                return 1  # Return 1 to indicate a valid decoding
            
            if s[0] == '0':
                return 0
            if len(s) == 1:
                return 1
            if s in memo:
                return memo[s]
            
            count = recursion(s[1:])
            if int(s[:2]) <= 26:
                count += recursion(s[2:])
            
            memo[s] = count
            return count
        
        return recursion(s)

