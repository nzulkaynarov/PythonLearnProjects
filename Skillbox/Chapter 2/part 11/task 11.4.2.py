class Coordinate:
    count = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Coordinate.count += 1

    def print_coordinate(self):
        print(self.x, self.y, Coordinate.count)

point = Coordinate(5, 6)
point_2 = Coordinate(1, 4)
point_3 = Coordinate(3, 6)
point_4 = Coordinate(1, 4)
point.print_coordinate()