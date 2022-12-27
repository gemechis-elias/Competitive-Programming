class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minimum= 10**4 + 1
        ans = -1
        for idx, coordinate in enumerate(points):
            if coordinate[0] == x:
                tmp = abs(y - coordinate[1])
                if tmp < minimum:
                    ans = idx
                    minimum = tmp
            if coordinate[1] == y:
                tmp = abs(x - coordinate[0])
                if tmp < minimum:
                    ans = idx
                    minimum = tmp
                
        return ans