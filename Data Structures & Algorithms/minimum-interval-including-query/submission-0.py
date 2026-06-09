import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries_with_index = [
            (q, i)
            for i, q in enumerate(queries)
        ]
        queries_with_index.sort()
        intervals.sort()
        open_intervals = [] # (len, end)

        res = [-1] * len(queries)
        interval_index = 0

        for q, i in queries_with_index:

            while interval_index < len(intervals) and intervals[interval_index][0] <= q:
                l, r = intervals[interval_index]
                length = r - l + 1
                heapq.heappush(open_intervals, (length, r))
                interval_index += 1
            
            while open_intervals and open_intervals[0][1] < q:
                heapq.heappop(open_intervals)
            
            
            res[i] = -1 if not open_intervals else open_intervals[0][0]
        
        return res