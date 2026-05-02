class MyHashSet:

    def __init__(self):
        self.array = []
    
    def add(self, key):
        if self.contains(key):
            return
        self.array.append(key)
        
    def contains(self, key) -> bool:
        return self.array.count(key) > 0
    
    def remove(self, key):
        pos = -1
        for i, value in enumerate(self.array):
            if value == key:
                pos = i
        if pos == -1:
            return
        self.array[-1], self.array[pos] = self.array[pos], self.array[-1]
        self.array.pop()
        # self.array = self.array[:i] + self.array[i+1:]



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(1)
# obj.contains(1) # true


# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)