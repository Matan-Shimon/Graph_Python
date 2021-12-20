from Point2D import  Point2D

class Node_Data:
    def __init__(self, point, weight, node_id, tag) -> None:
        self.weight = weight
        self.node_id = node_id
        self.point = point
        self.tag = tag
        #self.key_track = 0


    def getKey(self):
        return self.node_id


    def getPoint2D(self):
        return self.point

    def setPoint2D(self, otherPoint):
        self.point.setPoint(otherPoint)

    def getWeight(self):
        return self.weight

    def getTag(self):
        return self.tag

    def setWeight(self, w):
        self.weight = w

    def seTag(self, t):
        self.tag = t


if __name__ == '__main__':
    a = Node_Data(Point2D(1,1),4,0,0,0)
    print(a.point)
    a.setPoint2D(Point2D(2,2))
    print(a.point)

