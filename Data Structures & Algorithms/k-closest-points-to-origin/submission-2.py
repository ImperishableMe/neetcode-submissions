class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [
            (-(p[0] ** 2 + p[1] ** 2), p) 
            for p in points[:k]
        ]
        heapq.heapify(dist)
        for p in points[k:]:
            heapq.heappush(dist, (-(p[0] ** 2 + p[1] ** 2), p))
            heapq.heappop(dist)
            
        return [
           x
           for _, x in dist
        ]
