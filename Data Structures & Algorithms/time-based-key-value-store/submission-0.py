class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))
        # print(self.kv[key])

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        # print(self.kv[key])
        for (ts, val) in self.kv[key]:
            if timestamp >= ts:
                value = val
                # print ("values: ", ts, val)
        return value