class DSU:
    def __init__(self, n):
        self.n = n
        self.par = [0] * n
        self.sz = [1] * n
        for i in range(n):
            self.par[i] = i
    
    def find(self, node: int):
        self.par[node] = node if self.par[node] == node else self.find(self.par[node])
        return self.par[node]
    
    def merge(self, u: int, v: int) -> bool:
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return False
        if self.sz[u] < self.sz[v]:
            u, v = v, u
        
        self.par[v] = u
        self.sz[u] += self.sz[v]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        components = n

        for u, v in edges:
            if dsu.merge(u, v):
                components -= 1
        return components