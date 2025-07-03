from collections import defaultdict, Counter

class DetectSquares:
    def getddict(self):
        return defaultdict(list)

    def __init__(self):
        self.xy_dict = defaultdict(Counter)
        self.points = []

    def add(self, point: list[int]) -> None:
        self.points.append(point)
        self.xy_dict[point[0]][point[1]] += 1

    def count(self, point: list[int]) -> int:
        res = 0
        x, y = point
        for p in self.points:
            if abs(x - p[0]) == abs(y - p[1]) and abs(y - p[1]) != 0:
                x1, y1 = x, p[1]
                x2, y2 = p[0], y

                res += self.xy_dict[x1][y1] * self.xy_dict[x2][y2]

        return res        