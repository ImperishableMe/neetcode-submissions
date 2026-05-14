from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        temp_q = deque()
        while len(self.q) > 1:
            temp_q.append(self.q[0])
            self.q.popleft()
        val = self.q[0]
        self.q = temp_q
        return val

    def top(self) -> int:
        temp_q = deque()
        val = None
        while len(self.q) > 0:
            temp_q.append(self.q[0])
            val = self.q[0]
            self.q.popleft()
        self.q = temp_q
        assert val is not None
        return val

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()