from Point2D import  Point2D

class Node_Data:
    def __init__(self, point, weight, node_id, tag) -> None:
        self.weight = weight
        self.node_id = node_id
        self.point = point
        self.tag = tag


    def getKey(self):
        return self.node_id


    def getPoint2D(self):
        return self.point

    def setPoint2D(self, otherPoint):
        self.point.setPoint(otherPoint)

    def getWeight(self):
        return self.weight

    def geTag(self):
        return self.tag

    def setWeight(self, w):
        self.weight = w

    def seTag(self, t):
        self.tag = t

    def __lt__(self, other):
        return self.weight < other.weight


