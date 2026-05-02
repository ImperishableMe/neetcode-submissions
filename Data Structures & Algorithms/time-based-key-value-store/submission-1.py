class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))
        # print(self.kv[key])

    def get(self, key: str, timestamp: int) -> str:
        # arr = self.kv[key]
        if not key in self.kv:
            return ""
        arr = self.kv[key]
        lo, hi = 0, len(arr)
        # print(arr, key, timestamp)
        while lo < hi:
            mid = (lo + hi) >> 1
            # print(lo, hi, mid)
            if arr[mid][0] > timestamp:
                hi = mid
            else:
                lo = mid + 1
        if lo == 0:
            return ""
        return arr[lo-1][1] 