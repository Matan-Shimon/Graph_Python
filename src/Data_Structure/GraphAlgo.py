from src import GraphInterface
import heapq
import sys
from src.Data_Structure.Point2D import Point2D
from collections import deque
from src.Data_Structure.DiGraph import DiGraph
import json
import matplotlib.pyplot as plt
from matplotlib.widgets import *
from typing import List
import random

from src.Data_Structure.Node_Data import Node_Data


class GraphAlgo:
    def __init__(self, graph=DiGraph()) -> None:
        self.graph = graph
        self.ax = plt.subplot()

    def get_graph(self) -> GraphInterface:
        return self.graph
    """""
    this function clear the graph basically clearing the node's dict and the edge's dict
    """""
    def clear_graph(self):
        self.graph.edge_map.clear()
        self.graph.node_map.clear()
        self.graph.nodeSize = 0
        self.graph.edgeSize = 0

    """""
    This function set the value int the graph before using some function
    the function all the tag value to zero and the weight of the Node to MAX_VALUE
    """""
    def setValue(self):
        for i in range(0, self.graph.nodeSize):
            node = self.graph.get_node(i)
            node.seTag(0)
            node.setWeight(sys.maxsize)
        for i in range(0,self.graph.nodeSize):
            edge_dict = self.graph.all_out_edges_of_node(i)
            for j in edge_dict.keys():
                edge = self.graph.get_edge(i, j)
                edge.seTag(0)

    """""
    key Starting node
    This function finding the fastest route from node src to all other node in graph.
    along the way the function are uptading the node weight which represent how much time.
    it takes to reach from the node src to other node at the graph in the shortest way.
    the function will end when we reach all node we can go meaning there is a path.
    """""
    def Dijkstra(self, src):
        PQ = []
        self.setValue()
        self.graph.get_node(src).setWeight(0)
        node = self.graph.get_node(src)
        heapq.heapify(PQ)
        heapq.heappush(PQ, node)
        while(len(PQ)!=0):
            node_curr = heapq.heappop(PQ)
            node_src_id = node_curr.getKey()
            if(node_curr.geTag()!=1):
                edge_dic = self.graph.all_out_edges_of_node(node_src_id)
                for dest_id, weight in edge_dic.items():
                    node_dest = self.graph.get_node(dest_id)
                    edge_weight = weight
                    if(node_dest.geTag()!=1):
                        t = weight+node_curr.getWeight()
                        if(node_dest.getWeight()>t):
                            node_dest.setWeight(t)
                        heapq.heappush(PQ, node_dest)
            node_curr.seTag(1)
    """""
     The graph we want to transpose.
     we're changing the direction of the edge
     if the edge existed between two node for both way(a->b,b->) we are just swapping
     between the edge weight.
     if only one way existed between the node we're removing the edge and connect it the opposite way.
    """""
    def G_traspose(self):
        node_dic = self.graph.get_all_v().keys()
        for src in node_dic:
            edge = self.graph.all_out_edges_of_node(src)
            for dest, weight in edge.items():
                edge1 = self.graph.get_edge(src, dest)
                edge2 = self.graph.get_edge(dest, src)
                if(edge1 != None and edge2 != None and edge1.geTag()!= 1 and edge2.geTag()!= 1):
                    temp = edge1.getWeight()
                    edge1.setWeight(edge2.getWeight())
                    edge2.setWeight(temp)
                    edge1.seTag(1)
                    edge2.seTag(1)
                else:
                    if(edge1.geTag()!=1 and edge2 == None):
                        self.graph.remove_edge(src, dest)
                        self.graph.add_edge(dest, src, weight)
                        self.graph.get_edge(dest,src).seTag(1)

    """""
     The graph we are checking
     param node starting node for traversal
     the function doing the classic BFS
    """""
    def BFS(self, src):
        Q = deque()
        node = self.graph.get_node(src)
        node.seTag(1)
        Q.append(src)
        while(len(Q) != 0):
            curr = Q.popleft()
            edge_dic = self.graph.all_out_edges_of_node(curr)
            for dest,weight in edge_dic.items():
                if(self.graph.get_node(dest)!=None and self.graph.get_node(dest).geTag()==0):
                    self.graph.get_node(dest).seTag(1)
                    Q.append(dest)

    """""
     This function check if graph G is strongly connected
     we going to run DFS twice first time: starting from random vertex v if there is no path from 'v' to all node
     the graph is not connected. if there is path to every node  we going to run DFS for the second time but now for
     the graph G transpose and we gonna start DFS with 'v' and if in G transpose 'v' didnt reach all node
     it means that in the original graph G there is some vertix 'u' who dosent have a path from 'u' to 'v'
     there for the graph isnt connected if the graph pass both DFS means the graph strongly connected
    """""
    def isConnected(self) -> bool:
        if(self.graph.v_size==1):
            return True
        if(self.graph.v_size==0):
            return False
        self.setValue()
        node_dict = self.graph.get_all_v().keys()
        self.BFS(0)
        for i in node_dict:
            if(self.graph.get_node(i).geTag()==0):
                return False
        self.setValue()
        self.G_traspose()
        self.BFS(0)
        for i in node_dict:
            if(self.graph.get_node(i).geTag()==0):
                self.setValue()
                self.G_traspose()
                return False
        self.setValue()
        self.G_traspose()
        return True
    """""
     * @param id1 - start node
     * @param id2 - end (target) node
     * @return tuple first element the minimal time it take to reach from src to dest in the using Dijkstra
     * second element is a list representing the path between the two nodes
    """""
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        node_path_reverse = []
        self.Dijkstra(id1)
        dist = -1
        if self.graph.get_node(id2).getWeight() != sys.maxsize:
            dist = self.graph.get_node(id2).getWeight()
            self.G_traspose()
            node_first = self.graph.get_node(id2)
            node_path_reverse.append(node_first.node_id)
            while node_first.getKey() != id1:
                node_dict = self.graph.all_out_edges_of_node(node_first.getKey())
                for dest, weight in node_dict.items():
                    val = weight + self.graph.get_node(dest).getWeight()
                    if val == node_first.getWeight():
                        node_first = self.graph.get_node(dest)
                node_path_reverse.append(node_first.node_id)
            node_path_reverse.reverse()
            self.setValue()
            self.G_traspose()
            return dist, node_path_reverse
        else:
            return float('inf'), []
    """""
     * @return The node center and the radius of the graph
     * This function finding the center in the graph first we need to check if
     * the graph is connected if not we return null
     * after we check it we are going to call to shortestPathDist for each node
     * and then the weight going to be updated for all node we take the eccentricity which is the longest
     * distance between this node to other node
     * after we check all node we are going to choose the node with the smaller eccentricity and this node going to
     * be the center is graph.
    """""
    def centerPoint(self) -> (int, float):
        if self.isConnected() == False:
            return -1, -1.0
        index = 0
        min = sys.maxsize
        for i in range(0, self.graph.v_size()):
            self.Dijkstra(i)
            max = -sys.maxsize
            for j in range(0, self.graph.v_size()):
                dist = self.graph.get_node(j).getWeight()
                if max < dist:
                    max = dist
            if min > max:
                min = max
                index = i
        return index, min
    """""
     * This function return list of NodeData and float for the weight of this path 
     * the function gets a list of nodes that we are asking to travel somehow in the graph.
     * the function need to return a list of nodes which represent a path that are visiting
     * in all the node list we get and we need to find the path with the minimal time
     * if there is now path from nodes in the list we are getting we gonna return null
     * the function use dijkstra to hopefully find the shortest path
     * this is a greedy algorithm and the solution will not be always the best solution.
    """""
    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if len(node_lst) == 0:
            return None
        ans = []
        ans_weight = 0
        start = sys.maxsize
        min = sys.maxsize
        right_track = []
        for i in range(len(node_lst)):
            track = []
            count = 1
            index = node_lst[i]
            track.append(index)
            while (count < len(node_lst)):
                index = self.rec(index, track, node_lst)
                if index == -1:
                    break
                track.append(index)
                count += 1
            if index != -1:
                weight = 0
                for j in range(len(track) - 1):
                    short = self.shortest_path(track[j], track[j + 1])
                    weight += short[0]
                if weight < min:
                    right_track.clear()
                    min = weight
                    start = i
                    for j in range(len(track)):
                        right_track.append(track[j])
        ans_weight = min
        for i in range(len(right_track) - 1):
            l = self.shortest_path(right_track[i], right_track[i + 1])[1]
            if i == 0:
                for j in range(len(l)):
                    ans.append(l[j])
                    #ans.append(l[j].node_id)
            else:
                for j in range(1, len(l)):
                    ans.append(l[j])
                    #ans.append(l[j].node_id)
        if len(ans) == 0:
            return None
        return ans, ans_weight

    def rec(self, id, track, cities):
        self.Dijkstra(id)
        next_key = -1
        min = sys.maxsize
        for i in range(len(cities)):
            if cities[i] not in track:
                leng = self.graph.get_node(cities[i]).weight
                if leng < min:
                    min = leng
                    next_key = cities[i]
        return next_key
    """""
     * @param file - file name of JSON file
     * @return  true if we succeeded to load the graph from the json file to our graph.
    """""
    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r+") as f:
                self.clear_graph()
                my_g = json.load(f)
                edges = my_g["Edges"]
                nodes = my_g["Nodes"]
                for dic in nodes:
                    spl = []
                    if len(dic.keys()) < 2:
                        x = random.random()
                        y = random.random()
                        x *= 10
                        y *= 10
                        z = 0
                        spl.append(str(x))
                        spl.append(str(y))
                        spl.append(str(z))
                    else:
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
        except:
            print("wrong file path")
        return False

    """""
    * @param file - the file name (may include a relative path).
     * @return true if the graph has been saved to the file
     * false if something went worng.
    """""

    def save_to_json(self, file_name: str) -> bool:
        edges = self.graph.get_edges()
        nodes = self.graph.get_nodes()
        dic = {"Edges": edges, "Nodes": nodes}
        with open(file_name, 'w') as f:
            json.dump(dic, indent=2, fp=f)

    """""
        * @param event - the string of the given nodes (example: 4,2).
         the function draws the shortest path between the two nodes in green
    """""
    def draw_sp(self, event) -> None:
        data = eval(event)
        id1 = data[0]
        id2 = data[1]
        path = self.shortest_path(id1, id2)[1]
        for i in range(len(path) - 1):
            source = self.graph.get_node(path[i])
            source_pos = source.point
            source_x = source_pos.x
            source_y = source_pos.y
            desti = self.graph.get_node(path[i + 1])
            desti_pos = desti.point
            desti_x = desti_pos.x
            desti_y = desti_pos.y
            self.ax.annotate("", xy=(source_x, source_y), xytext=(desti_x, desti_y), arrowprops=dict(arrowstyle="<-", color="green"))
        plt.show()

    """""
        * @param event - the string of the given nodes (example: 2,9,7).
         the function draws the shortest path between the nodes in yellow
    """""
    def draw_tsp(self, event) -> None:
        data = list(eval(event))
        id1 = data[0]
        id2 = data[1]
        path = self.TSP(data)[0]
        for i in range(len(path) - 1):
            source = self.graph.get_node(path[i])
            source_pos = source.point
            source_x = source_pos.x
            source_y = source_pos.y
            desti = self.graph.get_node(path[i + 1])
            desti_pos = desti.point
            desti_x = desti_pos.x
            desti_y = desti_pos.y
            self.ax.annotate("", xy=(source_x, source_y), xytext=(desti_x, desti_y), arrowprops=dict(arrowstyle="<-", color="yellow"))
        plt.show()

    """""
         the function draws the current graph.
    """""
    def plot_graph(self) -> None:
        ps = []
        for src, node_data in self.graph.node_map.items():
            pos = node_data.point
            x, y = pos.x, pos.y
            ps.append(plt.plot(x, y, markersize=4, marker='o', color='blue')[0])
            plt.text(x, y, str(node_data.node_id), color="red", fontsize=12)
            for dest, edge_data in self.graph.edge_map[src].items():
                dest_data = self.graph.get_node(dest)
                pos_ = dest_data.point
                x_, y_ = pos_.x, pos_.y
                plt.annotate("", xy=(x, y), xytext=(x_, y_), arrowprops=dict(arrowstyle="<-"))
        center = self.centerPoint()[0]
        axButton1 = plt.axes([0.68, 0.92, 0.1, 0.04])  # left, bottom, width, height
        bt1 = Button(ax=axButton1, label='Center', hovercolor='Orange')

        """""
            * @param event - the event present that the button "original" has been clicked,
            and there for the function will apply directly.
             the function draws the center node in prange.
        """""
        def center_color(event):
            ps[center].set_color("orange")
            plt.draw()
        bt1.on_clicked(center_color)

        box_loc = plt.axes([0.18, 0.92, 0.17, 0.04])  # left, bottom, width, height
        text_box = TextBox(box_loc, 'Shortest_Path', initial="Insert id1,id2", hovercolor='green')
        text_box.on_submit(self.draw_sp)

        box_loc2 = plt.axes([0.41, 0.92, 0.25, 0.04])  # left, bottom, width, height
        text_box2 = TextBox(box_loc2, 'TSP', initial="Insert id1,id2,id3,..", hovercolor='yellow')
        text_box2.on_submit(self.draw_tsp)

        axButton4 = plt.axes([0.8, 0.92, 0.1, 0.04])  # left, bottom, width, height
        bt4 = Button(ax=axButton4, label='Original')

        """""
            * @param event - the event present that the button "original" has been clicked,
            and there for the function will apply directly.
             the function draws the original graph.
        """""
        def original_color(event):
            ps[center].set_color("blue")
            for src, node_data in self.graph.node_map.items():
                pos = node_data.point
                x, y = pos.x, pos.y
                plt.text(x, y, str(node_data.node_id), color="red", fontsize=12)
                for dest, edge_data in self.graph.edge_map[src].items():
                    dest_data = self.graph.get_node(dest)
                    pos_ = dest_data.point
                    x_, y_ = pos_.x, pos_.y
                    self.ax.annotate("", xy=(x, y), xytext=(x_, y_), arrowprops=dict(arrowstyle="<-"))
            plt.show()
        bt4.on_clicked(original_color)
        plt.show()

    def __str__(self):
        return self.graph


if __name__ == '__main__':
    algo = GraphAlgo()
    algo.load_from_json("C:\\Users\\matan\\PycharmProjects\\Graph_Python\\data\\A0.json")
    # print(algo.graph)
    algo.G_traspose()
    algo.setValue()
    algo.G_traspose()
    algo.save_to_json("check.json")
    # print(algo.centerPoint())
    algo.plot_graph()
    # node = Node_Data(Point2D(1, 1, 1), 10, 0, 0)
    # node1 = Node_Data(Point2D(1, 1,1), 4, 1, 0)
    # node2 = Node_Data(Point2D(1, 1,1), 3, 2, 0)
    # node3 = Node_Data(Point2D(1, 1,1), 1, 3, 0)
    # algo.graph.add_node(0, Point2D(0,0,0))
    # algo.graph.add_node(1, Point2D(10,10,0))
    # algo.graph.add_node(2, Point2D(3,3,0))
    # algo.graph.add_node(3, Point2D(15,2,0))
    # algo.graph.add_edge(0,1,4)
    # algo.graph.add_edge(1,0,3)
    # algo.graph.add_edge(1,3,5)
    # algo.graph.add_edge(3,2,7)
    # algo.plot_graph()
