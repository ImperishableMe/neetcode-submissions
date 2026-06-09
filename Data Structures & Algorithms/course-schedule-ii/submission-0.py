class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for after, before in prerequisites:
            indegree[after] += 1
            graph[before].append(after)
        
        q = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        order = []
        while q:
            course = q.popleft()
            order.append(course)
            for out in graph[course]:
                indegree[out] -= 1
                if indegree[out] == 0:
                    q.append(out)
            
        return order if len(order) == numCourses else [] 