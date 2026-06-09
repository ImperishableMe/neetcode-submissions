"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)
        endings = []

        for interval in intervals:
            if endings and endings[0] <= interval.start:
                heapq.heappop(endings)
            heapq.heappush(endings, interval.end)
        return len(endings)