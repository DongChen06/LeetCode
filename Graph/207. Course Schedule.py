class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        graph = {i: [] for i in range(numCourses)}

        # build the map
        for c, p in prerequisites:
            graph[c].append(p)

        def dfs(graph, start):
            visited, stack = set([start]), [start]

            while stack:
                node = stack.pop()
                for n in graph[node]:
                    if n in visited:
                        return False
                    visited.add(n)
                    stack.append(n)
            return True

        for c in range(numCourses):
            if not dfs(graph, c):
                return False
        return True


s = Solution()

print(s.canFinish(2, [[1, 0]]))  # true
print(s.canFinish(2, [[1, 0], [0, 1]]))  # false
print(s.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))  # true
print(s.canFinish(20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]))  # false
