class MyHashMap:
    BUCKET_SIZE = 10000

    def __init__(self, bs = BUCKET_SIZE):
        self.bs = bs
        self.buckets = [[] for _ in range(bs)]

    def _bucket_id(self, key):
        return hash(key) % self.bs

    def put(self, key: int, value: int) -> None:
        bid = self._bucket_id(key)
        pos = -1
        for i, bv in enumerate(self.buckets[bid]):
            if bv[0] == key:
                pos = i
        if pos == -1:
            self.buckets[bid].append((key, value))
        else:
            self.buckets[bid][pos] = (key, value)
        

    def get(self, key: int) -> int:
        bucket_id = self._bucket_id(key)
        for (b_key, b_value) in self.buckets[bucket_id]:
            if b_key == key:
                return b_value
        else:
            return -1
    
    
    def remove(self, key) -> None:
        bid = self._bucket_id(key)
        pos = -1
        for i, value in enumerate(self.buckets[bid]):
            if value[0] == key:
                pos = i
        if pos == -1:
            return
        self.buckets[bid][-1], self.buckets[bid][pos] = self.buckets[bid][pos], self.buckets[bid][-1]
        self.buckets[bid].pop()
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)