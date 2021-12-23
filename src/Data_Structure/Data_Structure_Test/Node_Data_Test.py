import unittest

from src.Data_Structure.Node_Data import Node_Data
from src.Data_Structure.Point2D import Point2D


class MyTestCase(unittest.TestCase):
    node = Node_Data(Point2D(1,1,1),3,0,0)

    def test_getPoint2D(self):
        P = Point2D(1,1,1)
        self.assertEqual(P.x,self.node.getPoint2D().x)
        self.assertEqual(P.y, self.node.getPoint2D().y)
        self.assertEqual(P.z, self.node.getPoint2D().z)

    def test_Weight(self):
        self.assertEqual(self.node.getWeight(),3)
