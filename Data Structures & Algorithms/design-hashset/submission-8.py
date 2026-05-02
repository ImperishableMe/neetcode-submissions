class MyHashSet:
    N = 10**6
    BLOCK_SIZE = 32
    SZ = (N + BLOCK_SIZE - 1) // BLOCK_SIZE

    def __init__(self):
        print(self.SZ)
        self.buckets = [0] * (self.SZ)
    
    def _get_mask(self, key: int) -> int:
        return 1 << (key % self.BLOCK_SIZE)

    def add(self, key: int) -> None:
        bit_index = key // self.BLOCK_SIZE
        self.buckets[bit_index] |= self._get_mask(key);

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        self.buckets[key // self.BLOCK_SIZE] ^= self._get_mask(key);

    def contains(self, key: int) -> bool:
        return self.buckets[key // self.BLOCK_SIZE] & self._get_mask(key) != 0;
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)