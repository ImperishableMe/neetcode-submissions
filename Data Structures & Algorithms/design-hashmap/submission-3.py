class MyHashMap:
    NUMBER_OF_BUCKETS = 10000

    def __init__(self):
        self.buckets: list[list[tuple(int, int)]] = [[] for _ in range(self.NUMBER_OF_BUCKETS)]

    def _get_bucket(self, key) -> list[tuple(int, int)]:
        return self.buckets[key % self.NUMBER_OF_BUCKETS]

    # def _contains(self, key: int) -> None:

    def put(self, key: int, value: int) -> None:
        bucket = self._get_bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket = self._get_bucket(key)
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        bucket = self._get_bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
        return        




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)