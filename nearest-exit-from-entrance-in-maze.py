class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([tuple(entrance)])
        maze[entrance[0]][entrance[1]] = '+'
        directions =  [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < len(maze) and 0 <= col < len(maze[0]))
        distance = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    
                    if not inbound(new_row, new_col):
                        if distance:
                            return distance
                        if (row, col) != tuple(entrance):
                            return -1
                        continue

                    if maze[new_row][new_col] == '.':
                        maze[new_row][new_col] = '+'
                        queue.append((new_row, new_col))

            distance += 1
        return -1