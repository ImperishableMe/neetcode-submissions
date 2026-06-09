"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        class Event:
            def __init__(self, ts: int, e_type: int):
                self.ts = ts
                self.e_type = e_type
            
            def __lt__(self, other: 'Event') -> bool:
                if self.ts == other.ts:
                    return self.e_type < other.e_type
                return self.ts < other.ts
        
        events = []
        for interval in intervals:
            events.append(Event(interval.start, 1))
            events.append(Event(interval.end, 0))
        
        events.sort()
        
        max_room_required = 0
        cur_needed = 0

        for e in events:
            e_type = e.e_type
            if e_type == 1:
                cur_needed += 1
            else:
                cur_needed -= 1
            max_room_required = max(max_room_required, cur_needed)

        return max_room_required


