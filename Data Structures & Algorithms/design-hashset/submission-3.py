class MyHashSet:
    BUCKET_SIZE = 10000

    def __init__(self, bs = BUCKET_SIZE):
        self.bs = bs
        self.buckets = [[] for _ in range(bs)]
    
    def _bucket_id(self, key):
        return hash(key) % self.bs

    def add(self, key):
        if self.contains(key):
            return
        bucket_id = self._bucket_id(key)
        self.buckets[bucket_id].append(key)
        # self.array.append(key)
        
    def contains(self, key) -> bool:
        bucket_id = self._bucket_id(key)
        for b_key in self.buckets[bucket_id]:
            if b_key == key:
                return True
        else:
            return False
        
    
    def remove(self, key):
        bid = self._bucket_id(key)


        pos = -1
        for i, value in enumerate(self.buckets[bid]):
            if value == key:
                pos = i
        if pos == -1:
            return
        self.buckets[bid][-1], self.buckets[bid][pos] = self.buckets[bid][pos], self.buckets[bid][-1]
        self.buckets[bid].pop()
        # self.array = self.array[:i] + self.array[i+1:]



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(1)
# obj.contains(1) # true


# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)