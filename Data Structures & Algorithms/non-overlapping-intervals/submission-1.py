class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda p: (p[1], p[0]))
        # kept_intervals = [intervals[0]]
        last_en = intervals[0][1]
        kept = 1
        for i in range(1, len(intervals)):
            st, en = intervals[i]
            if st < last_en:
                continue
            last_en = en
            kept += 1
            # kept_intervals.append([st, en])
        return len(intervals) - kept
