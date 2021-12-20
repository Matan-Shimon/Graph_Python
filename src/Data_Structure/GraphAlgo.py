import matplotlib.pyplot as plt
import json
from DiGraph import DiGraph
from Point2D import Point2D
from src import GraphInterface
import sys
import heapq
from typing import List
from collections import deque

class GraphAlgo:
    def __init__(self, graph=DiGraph()):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def setValue(self):
        node_dic = self.graph.get_all_v
        for i in node_dic:
            node = self.graph.get_node(i)
            node.seTag(0)
            node.seWeight(sys.maxsize)

    def BFS(self, src):
        Q = deque()
        node = self.graph.get_node(src)
        node.seTag(1)
        Q.append(src)
        while (Q.qsize() != 0):
            curr = Q.popleft()
            edge_dic = self.graph.all_out_edges_of_node(curr)
            for dest, weight in edge_dic.items():
                if (self.graph.get_node(dest) != None and self.graph.get_node(dest).geTag() == 0):
                    self.graph.get_node(dest).seTag(1)
                    Q.append(dest)

    def Dijkstra(self, src):
        PQ = []
        self.setValue()
        self.graph.get_node.setWeight(0)
        heapq.heapify(PQ)
        heapq.heappush(PQ, src)
        while (len(PQ) != 0):
            nodeId = PQ.pop()
            nodeSrc = self.graph.get_node(nodeId)
            if (nodeSrc.geTag() != 1):
                edge_dic = self.graph.all_out_edges_of_node(nodeId)
                for destId, weight in edge_dic.items():
                    nodeDest = self.graph.get_node(destId)
                    edge_weight = weight
                    if (nodeDest.geTag() != 1):
                        t = weight + nodeSrc.getWeight()
                        if (nodeDest.getWeight() > t):
                            nodeDest.setWeight(t)
                    heapq.heappush(PQ, destId)
            nodeSrc.seTag(1)

    def G_traspose(self):
        node_dic = self.graph.get_all_v.keys
        for src in node_dic:
            edge = self.graph.all_out_edges_of_node(src)
            for dest, weight in edge.items():
                edge1 = self.graph.get_edge(src, dest)
                edge2 = self.graph.get_edge(dest, src)
                if (edge1 != None and edge2 != None and edge1.geTag() != 1 and edge2.geTag() != 1):
                    temp = edge1.getWeight
                    edge1.setWeight(edge2.getWeight())
                    edge2.setWeight(edge1.getWeight())
                    edge1.seTag(1)
                    edge2.seTag(1)
                else:
                    if (edge1.geTag() != 1 and edge2 == None):
                        self.graph.remove_edge(src, dest)
                        self.graph.add_edge(dest, src, weight)
                        edge2.seTag(1)

    def shortest_path(self, id1: int, id2: int) -> (float,list):
        node_path_reverse = []
        dist = self.Dijkstra(id1)
        if (self.graph.get_node(id2).getWeight != sys.maxsize):
            self.G_traspose()
            node_first = self.graph.get_node(id2)
            node_path_reverse.append(node_first)
            while (node_first.getKey() != id1):
                node_dict = self.graph.all_out_edges_of_node(node_first.getKey())
                for dest, weight in node_dict.items():
                    val = weight + self.graph.get_node(dest).getWeight()
                    if (val == node_first.getWeight()):
                        node_first = self.graph.get_node(dest)
                node_path_reverse.append(node_first)
            node_path_reverse.reverse()
            self.G_traspose()
            return float(dist), node_path_reverse
        else:
            return sys.maxsize, node_path_reverse

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if len(node_lst) == 0:
            return None
        ans = List[int]()
        ans_weight = 0
        start = sys.maxsize
        min = sys.maxsize
        right_track = []
        for i in range(len(node_lst)):
            track = []
            count = 1
            index = node_lst[i]
            track.append(index)
            while(count < len(node_lst)):
                index = self.rec(index, track, node_lst)
                if index == -1:
                    break
                track.append(index)
                count += 1
            if index != -1:
                weight = 0
                for j in range(len(track)-1):
                    weight += self.shortest_path(track[j], track[j+1])[0]
                if weight < min:
                    right_track.clear()
                    min = weight
                    start = i
                    for j in range(len(track)):
                        right_track.append(track[j])
        ans_weight = min
        for i in range(len(right_track)-1):
            l = self.shortest_path(right_track[i], right_track[i+1])[1]
            if i == 0:
                for j in range(len(l)):
                    ans.append(l[j])
            else:
                for j in range(1, len(l)):
                    ans.append(l[j])
        if len(ans) == 0:
            return None
        return ans, ans_weight

    def rec(self, id, track, cities):
        self.Dijkstra(id)
        next_key = -1
        min = sys.maxsize
        for i in range(len(cities)):
            if cities[i] not in track:
                len = self.graph.get_node(cities[i]).weight
                if len < min:
                    min = len
                    next_key = cities[i]
        return next_key

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name,"r+") as f:
            my_g = json.load(f)
            edges = my_g["Edges"]
            nodes = my_g["Nodes"]
            print(edges)
            for dic in nodes:
                spl = dic["pos"].split(",")
                id = dic["id"]
                pos = Point2D(float(spl[0]), float(spl[1]), float(spl[2]))
                self.graph.add_node(id, pos)
            for dic in edges:
                src = dic["src"]
                dest = dic["dest"]
                weight = dic["w"]
                self.graph.add_edge(int(src), int(dest), float(weight))
            return True
        return False

    def save_to_json(self, file_name: str) -> bool:
        edges = self.graph.get_edges()
        nodes = self.graph.get_nodes()
        dic = {"Edges":edges,"Nodes":nodes}
        with open(file_name, 'w') as f:
            json.dump(dic, indent=2, fp=f)

    def plot_graph(self) -> None:
        for src,node_data in self.graph.node_map.items():
            pos = node_data.point
            x, y = pos.x, pos.y
            plt.plot(x, y, markersize=4, marker='o', color='blue')
            plt.text(x, y, str(node_data.node_id), color="red", fontsize=12)
            for dest, edge_data in self.graph.edge_map[src].items():
                dest_data = self.graph.get_node(dest)
                pos_ = dest_data.point
                x_, y_ = pos_.x, pos_.y
                plt.annotate("", xy=(x, y), xytext=(x_, y_), arrowprops=dict(arrowstyle="<-"))
        plt.show()

    def __str__(self):
        return self.graph

if __name__ == '__main__':
    algo = GraphAlgo()
    algo.load_from_json("C:\\Users\\matan\\PycharmProjects\\Graph_Python\\data\\A0.json")
    print(algo.graph)
    algo.save_to_json("check.json")
    algo.plot_graph()