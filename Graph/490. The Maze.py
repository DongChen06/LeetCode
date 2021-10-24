class Solution:
    def hasPath(self, maze, start, destination):
        '''
        Detailed explanation is available at
        https://medium.com/@edward.zhou/leet-code-53-maximum-subarray-detailed-explained-python3-solution-d91c7affc02a
        '''

        visited = []
        row, col = len(maze), len(maze[0])
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        des = (destination[0], destination[1])

        def dfs(stop):
            stops = []
            for dir in dirs:
                new_x, new_y = stop[0], stop[1]
                while True:
                    nx = new_x + dir[0]
                    ny = new_y + dir[1]
                    if 0 <= nx < row and 0 <= ny < col and maze[nx][ny] != 1:
                        new_x, new_y = nx, ny
                    else:
                        break
                if (new_x, new_x) == des:
                    return True
                stops.append((new_x, new_y))

            visited.append(stop)
            for node in stops:
                if node not in visited:
                    if dfs(node):
                        return True
            return False

        return dfs((start[0], start[1]))


s = Solution()
maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
start = [0, 4]
des = [4, 4]
print(s.hasPath(maze, start, des))
