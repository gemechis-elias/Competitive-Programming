class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        visited = set(deadends)
        queue = deque([('0000', 0)])

        while queue:
            curr, moves = queue.popleft()

            if curr == target:
                return moves

            for i in range(4):
                digit = int(curr[i])

                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    new_combo = curr[:i] + str(new_digit) + curr[i+1:]

                    if new_combo not in visited:
                        visited.add(new_combo)
                        queue.append((new_combo, moves + 1))

        return -1