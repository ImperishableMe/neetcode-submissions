from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.versionMap: Dict[int, List[Tuple[int, int]]] = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.versionMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        versions = self.versionMap[key]
        index = bisect_right(versions, timestamp, key=lambda p: p[0])
        return versions[index - 1][1] if index > 0 else ""

        
