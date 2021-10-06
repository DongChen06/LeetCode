"""
ref: https://github.com/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Graphs/Implementation%20of%20Depth%20First%20Search.ipynb
"""

from collections import deque

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}


def dfs(graph, start):
    visited, stack = set(), [start]

    while stack:
        node = stack.pop()
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                stack.append(n)
    return visited


def dfs_path(graph, start, target):
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()
        for n in graph[node]:
            if n not in path:
                if n == target:
                    yield path + [n]
                else:
                    stack.append([n, path + [n]])


def dfs_dp(graph, node, visited):
    if not visited:
        visited = []

    if node not in visited:
        visited.append(node)

        for nei in graph[node]:
            dfs_dp(graph, nei, visited)
    return visited


def bfs(graph, start):
    visited, queue = set(), deque([start])

    while queue:
        node = queue.pop()
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.appendleft(n)
    return visited


# print(dfs(graph, "A"))
# print(dfs(graph, "C"))
# print(list(dfs_path(graph, "A", "F")))
#
#
# print(bfs(graph, "A"))
# print(bfs(graph, "C"))
print(dfs_dp(graph, "A", None))
