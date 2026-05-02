class MyHashSet:
    NUMBER_OF_BUCKETS = 10000

    def __init__(self):
        self.buckets = [[] for _ in range(self.NUMBER_OF_BUCKETS)]

    def _get_bucket(self, key) -> list[int]:
        return self.buckets[hash(key) % self.NUMBER_OF_BUCKETS]

    def add(self, key: int) -> None:
        bucket = self._get_bucket(key)
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self._get_bucket(key)
        try:
            bucket.remove(key)
        except ValueError:
            return

    def contains(self, key: int) -> bool:
        return key in self._get_bucket(key)
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)