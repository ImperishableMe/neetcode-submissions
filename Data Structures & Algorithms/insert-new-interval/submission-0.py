class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        [nl, nr] = newInterval
        left_intervals, right_intervals = [], []

        for [l, r] in intervals:
            if l > nr:
                right_intervals.append([l, r])
            elif r < nl:
                left_intervals.append([l, r])
            else:
                nl = min(nl, l)
                nr = max(nr, r)
        return left_intervals + [[nl, nr]] + right_intervals