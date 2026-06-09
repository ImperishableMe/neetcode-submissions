class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for after, before in prerequisites:
            indegree[after] += 1
            graph[before].append(after)
        
        q = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        can_take = 0
        while q:
            course = q.popleft()
            can_take += 1
            for out in graph[course]:
                indegree[out] -= 1
                if indegree[out] == 0:
                    q.append(out)
            
        return can_take == numCourses
