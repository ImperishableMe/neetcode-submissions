class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [
            (p[0]** 2 +  p[1]** 2, p) 
            for p in points
        ]
        heapq.heapify(dist)
        return [heapq.heappop(dist)[1] for i in range(k)]
