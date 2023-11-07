class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point):
        x, y = point
        if (x, y) not in self.points:
            self.points[(x, y)] = 1
        else:
            self.points[(x, y)] += 1

    def count(self, point):
        x, y = point
        count = 0
        for (x2, y2), freq in self.points.items():
            dy = abs(y - y2)
            dx = abs(x - x2)
            if dy == dx and dx > 0:
                if (x, y2) in self.points and (x2, y) in self.points:
                    count += freq * self.points.get((x, y2), 0) * self.points.get((x2, y), 0)
        return count
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)