import unittest

from src.Data_Structure.DiGraph import DiGraph
from src.Data_Structure.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    algo = GraphAlgo()

    def test_center(self):
        self.algo.load_from_json("C:\\Users\\yarin\\Desktop\\10000Nodes.json")
        # self.algo.G_traspose()
        # self.algo.setValue()
        # self.algo.G_traspose()
        # self.algo.save_to_json("a.json")
        # self.assertEqual(1,1)
        print(self.algo.centerPoint())
    def test_isConnected(self):
        self.algo.load_from_json("C:\\Users\\yarin\\Desktop\\10000Nodes.json")
        # print(self.algo.isConnected())

    def test_shortestPath(self):
        self.algo.load_from_json("C:\\Users\\yarin\\Desktop\\1000Nodes.json")
        print(self.algo.shortest_path(8,48))

    def test_transpose(self):
        self.algo.load_from_json("C:\\Users\\yarin\\Desktop\\10000Nodes.json")
        self.algo.G_traspose()


    def test_TSP(self):
        self.algo.load_from_json("C:\\Users\\yarin\\Desktop\\1000Nodes.json")
        l =[]
        l.append(100)
        l.append(200)
        l.append(300)
        print(self.algo.TSP(l))


