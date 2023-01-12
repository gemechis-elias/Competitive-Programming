class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i for i in range(1, n+1)]
        start = 0
        while len(circle) > 1:
            start = (start + k - 1) % len(circle)
            circle.pop(start)
        return circle[0]
