# 76. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring of s such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# TIME AND SPACE COMPLEXITY
# The time complexity of the minimum window substring problem is O(N), where N is the length of the string s. This is because in the worst case, each character in s will be visited twice, once by the right pointer (when we expand the window) and once by the left pointer (when we contract the window).
# The space complexity is O(M), where M is the number of unique characters in the string t. This is because we store the frequency of characters of t in a dictionary. In the worst case, when all characters in t are unique, the space complexity would be O(M).

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return "" # return empty if s is less than t in length

        tdict = defaultdict(int) # create dict for t
        window = defaultdict(int) # create dict for window

        # fill tdict with count of its chars
        for c in t:
            tdict[c] += 1 

        # initialize pointers
        left = 0 # left pointer of window
        count = 0 # count of t's chars in window
        min_len = float('inf') # len of window
        start = 0 # start to hold the start of last min window

        for right in range(len(s)): # for chars in s
            r = s[right] 

            window[r] += 1 # add char to window

            if r in tdict and window[r] <= tdict[r]: # if current char exist in t and it's count if less or equal in current window
                count += 1

            # while all t's chars exist in current window move left pointer to shorten the window
            while count == len(t):
                # update current min len
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left # remember start min window

                l = s[left] # left char
                left += 1 # move left pointer

                if l in tdict: # if left char exist in t and in curr window, remove it from window and decrease count 
                    if window[l] == tdict[l]:
                        count -= 1
                    window[l] -= 1

        return "" if min_len == float('inf') else s[start: start+min_len]



                




        



