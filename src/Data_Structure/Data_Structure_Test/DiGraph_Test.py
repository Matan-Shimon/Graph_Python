import unittest

from src.Data_Structure.DiGraph import DiGraph
from src.Data_Structure.Node_Data import Node_Data
from src.Data_Structure.Point2D import Point2D


class MyTestCase(unittest.TestCase):
  graph = DiGraph()
  graph.add_node(Point2D(1, 1, 1), 0)
  graph.add_node(Point2D(2, 2, 2), 1)
  graph.add_node(Point2D(3, 3, 3), 2)
  graph.add_node(Point2D(4, 4, 4), 3)
  def test_addNode(self):
      self.assertEqual(self.graph.nodeSize,4)
      self.graph.add_node(Point2D(1, 1, 1), 4)
      self.assertEqual(self.graph.nodeSize, 5)




