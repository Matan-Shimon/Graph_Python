import unittest

from src.Data_Structure.DiGraph import DiGraph
from src.Data_Structure.Node_Data import Node_Data
from src.Data_Structure.Point2D import Point2D


class MyTestCase(unittest.TestCase):
  graph = DiGraph()
  graph.add_node(0, Point2D(1, 1, 1))
  graph.add_node(1, Point2D(1, 1, 1))
  graph.add_node(2, Point2D(1, 1, 1))
  graph.add_node(3, Point2D(1, 1, 1))
  def test_addNode(self):
      self.assertEqual(self.graph.nodeSize,4)
      self.graph.add_node(Point2D(1, 1, 1), 4)
      self.assertEqual(self.graph.nodeSize, 5)

  def test_addEdge(self):
      print(self.graph.nodeSize)
      print(self.graph.get_node(2))
      self.graph.add_edge(1,2,2)
      self.assertEqual(self.graph.get_edge(1,2).getWeight(),2)

  def test_removeNode(self):
      self.graph.add_edge(0, 1, 2)
      self.graph.add_edge(0, 2, 2)
      self.graph.add_edge(0, 3, 2)
      self.assertEqual(self.graph.get_edge(0, 1).getWeight(), 2)
      self.graph.remove_node(0)
      self.assertEqual(self.graph.nodeSize,3)
      self.assertEqual(self.graph.get_edge(0,1),None)




