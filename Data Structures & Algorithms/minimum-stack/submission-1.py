class MinStack:
    def __init__(self):
        self.st = [] # (val, min_so_far)        

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append((val, val))
        else:
            _, min_so_far = self.st[-1]
            self.st.append((val, min(val, min_so_far)))
        

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
