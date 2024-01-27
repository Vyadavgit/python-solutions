
#  Q57. Insert Interval
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

#         Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

#         Return intervals after the insertion.

#         Example 1:

#         Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#         Output: [[1,5],[6,9]]

#  Time complexity: O(n)
#  Space complexity: O(n)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0

        # add all intervals till newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # merge all overlaps to a newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        # add merged list
        res.append(newInterval)

        # add remaining
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res



        