"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i : i.start)

        for i in range(1, len(intervals)):
            int1 = intervals[i]
            int2 = intervals[i-1]

            if int2.end > int1.start:
                return False
        return True

