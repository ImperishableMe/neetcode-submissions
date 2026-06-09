import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
            if i < k - 1:
                continue
            left = i - k
            while heap and heap[0][1] <= left:
                heapq.heappop(heap)

            res.append(-heap[0][0])

        assert len(res) == len(nums) - k + 1  
        return res      