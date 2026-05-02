class MyHashSet:
    NUMBER_OF_BUCKETS = 10000

    def __init__(self):
        self.buckets = [[] for _ in range(MyHashSet.NUMBER_OF_BUCKETS)]

    def _get_bucket(self, key) -> int:
        return hash(key) % MyHashSet.NUMBER_OF_BUCKETS

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        bucket = self.buckets[self._get_bucket(key)]
        bucket.append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        bucket = self.buckets[self._get_bucket(key)]
        bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[self._get_bucket(key)]
        for elem in bucket:
            if elem == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)