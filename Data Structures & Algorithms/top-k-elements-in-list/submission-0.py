class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
        arr = [(v, k) for k, v in cnt.items()]
        arr.sort(reverse=True)
        arr = arr[:k]
        return [el[1] for el in arr]