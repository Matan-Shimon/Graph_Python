
class Point2D:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def setPoint(self, other):
        self.x = other.x
        self.y = other.y

    def __str__(self) -> str:
        return f"X = {self.x} Y={self.y}"

