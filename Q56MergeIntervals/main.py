# Q56. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of
# the non-overlapping intervals that cover all the intervals in the input.

#         Example 1:

#         Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#         Output: [[1,6],[8,10],[15,18]]
#         Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        merged = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if prev[1] >= interval[0]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval
        merged.append(prev)

        return merged