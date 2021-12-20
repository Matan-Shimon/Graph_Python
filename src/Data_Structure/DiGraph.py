from Node_Data import Node_Data
from Edge_Data import Edge_Data
class DiGraph:
    def __init__(self, nodeSize=0, edgeSize=0, node_map={}, edge_map={}, MC=0) -> None:
        self.nodeSize = nodeSize
        self.edgeSize = edgeSize
        self.MC = MC
        self.node_map = {}
        self.edge_map = {}

    def v_size(self) -> int:
        return self.nodeSize

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.node_map

    def get_node(self, id):
        try:
            return self.node_map[id]
        except:
            return None

    def get_edge(self, src_id, dest_id):
        try:
            return self.edge_map[src_id][dest_id]
        except:
            return None

    def all_in_edges_of_node(self, id1: int) -> dict:
        inside = {}
        node_keys = self.node_map.keys()
        for i in node_keys:
            if self.get_edge(i, id1) != None:
                inside[i] = self.get_edge(i, id1).getWeight()
        return inside

    def all_out_edges_of_node(self, id1: int) -> dict:
        outside = {}
        for dest_key, edge_data in self.edge_map[id1].items():
            outside[dest_key] = edge_data.getWeight()
        return outside

    def get_mc(self) -> int:
        return self.MC

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.get_node(node_id) != None:
            print("The node is already exist")
            return False
        else:
            node_data = Node_Data(pos, 0, self.nodeSize, 0)
            self.node_map[node_id] = node_data
            self.edge_map[node_id] = {}
            self.nodeSize += 1
            self.MC += 1
            return True

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if weight >= 0:
            if self.get_node(id1) == None or self.get_node(id1) == None:
                print("One or more of the given nodes is not exist")
                return False
            else:
                if self.get_edge(id1,id2) != None:
                    print("The edge is already exists")
                    return False
                else:
                    edge_data = Edge_Data(id1, id2, weight, 0)
                    self.edge_map[id1][id2] = edge_data
                    self.edgeSize += 1
                    self.MC += 1
                    return True
        else:
            print("Edge weight cannot be negative")
            return False

    def remove_node(self, node_id: int) -> bool:
        if self.get_node(node_id) == None:
            print("The node does not exist")
            return False
        else:
            # removing all the out edges
            self.edge_map.pop(node_id)
            # removing all the in edges
            node_keys = self.node_map.keys()
            for node in node_keys:
                if self.get_edge(node, node_id) != None:
                    self.edge_map[node].pop(node_id)

            # removing the node itself
            self.node_map.pop(node_id)
            self.nodeSize -= 1
            self.MC += 1
            return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.get_edge(node_id1, node_id2) == None:
            print("The edge does not exist")
            return False
        else:
            self.edge_map[node_id1].pop(node_id2)
            self.edgeSize -= 1
            self.MC += 1
            return True

    def get_nodes(self):
        nodes = []
        for id,node_data in self.node_map.items():
            pos = f"{node_data.point.x},{node_data.point.y},{node_data.point.z}"
            dic = {"pos":pos,"id":id}
            nodes.append(dic)
        return nodes

    def get_edges(self):
        edges = []
        for src,src_edges in self.edge_map.items():
            for dest, edge_data in src_edges.items():
                dic = {"src":src,"w":edge_data.weight,"dest":dest}
                edges.append(dic)
        return edges

    def __str__(self):
        return str(self.edge_map)

if __name__ == '__main__':
    graph = DiGraph()
    graph.add_node(1, (1,1))
    graph.add_node(2, (2,2))
    graph.add_node(3, (2,1))
    graph.add_node(4, (1,2))
    graph.add_edge(1,2, 5)
    graph.add_edge(1,3, 5)
    graph.add_edge(2,4, 5)
    graph.add_edge(4,1, 5)
    print("in: ",graph.all_in_edges_of_node(1))
    print("out: ",graph.all_out_edges_of_node(1))
    print(graph.edge_map)
    graph.remove_edge(2,4)
    print(graph.edge_map)
    graph.add_edge(3,2, 5)
    graph.remove_node(1)
    print(graph.edge_map)

