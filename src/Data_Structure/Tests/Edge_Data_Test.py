import unittest

from src.Data_Structure.Edge_Data import Edge_Data


class MyTestCase(unittest.TestCase):
    edge = Edge_Data(0,1,10,0)
    edge1 = Edge_Data(2, 3, 9, 1)


    def test_getWeigth(self):
        self.assertEqual(self.edge.getWeight(),10)
        self.assertEqual(self.edge1.getWeight(), 9)
